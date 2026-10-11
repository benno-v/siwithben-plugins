#!/usr/bin/env python3
"""Read, write and check TASKS.md, the task tracker's single source of truth.

Python 3 standard library only. Also imported by render_dashboard.py and apply_changes.py.

Commands:
  tasks_md.py init      --tasks TASKS.md   create an empty TASKS.md (never overwrites)
  tasks_md.py validate  --tasks TASKS.md   list errors and warnings (exit 1 on errors)
  tasks_md.py revision  --tasks TASKS.md   print the 12-character revision of the task tables
  tasks_md.py show      --tasks TASKS.md   print every row as JSON (for de-duplication)
  tasks_md.py normalise --tasks TASKS.md   rewrite the tables in canonical form (keeps a backup)

Every write keeps the previous version in .task-tracker-backups/ next to TASKS.md (the last 5).
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
from pathlib import Path

MARKER = "<!-- task-tracker v1 -->"
COLUMNS = ["ID", "Action", "Owner", "Source", "Raised", "Due", "Status", "Notes"]
FIELDS = ["id", "action", "owner", "source", "raised", "due", "status", "notes"]
SECTION_TITLES = {"open": "Open", "proposed": "Proposed, needs approval", "done": "Done"}
LOG_TITLE = "Change log"
OPEN_STATUSES = ["Open", "In progress", "Waiting", "Blocked"]
SECTION_STATUSES = {"open": OPEN_STATUSES, "proposed": ["Proposed"], "done": ["Done"]}
ID_RE = re.compile(r"^T-(\d{3,})$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DONE_NOTE_RE = re.compile(r"\bdone (\d{4}-\d{2}-\d{2})\b")
LAST_SWEEP_RE = re.compile(r"^Last sweep:\s*(.*)$")
SEPARATOR_RE = re.compile(r"^\|[\s:|-]+\|$")
LOOSE_ROW_RE = re.compile(r"^\s*(\||T-\d{3,}\s*\|)")
BACKUP_DIR = ".task-tracker-backups"
BACKUPS_KEPT = 5

TEMPLATE = f"""# Tasks

{MARKER}
Last sweep: never

One list for every committed action, whatever app it came from. Edit it by hand if you like, but keep the
table columns. Owner blank means unassigned. Dates are YYYY-MM-DD. The Source column says where each task
came from, so you can check the owner and due date before they go into a report.

## Open

| ID | Action | Owner | Source | Raised | Due | Status | Notes |
|---|---|---|---|---|---|---|---|

## Proposed, needs approval

| ID | Action | Owner | Source | Raised | Due | Status | Notes |
|---|---|---|---|---|---|---|---|

## Done

| ID | Action | Owner | Source | Raised | Due | Status | Notes |
|---|---|---|---|---|---|---|---|

## Change log
"""


class ParseError(ValueError):
    pass


class Section:
    """kind is open, proposed, done, log or other. Task sections keep text around the table as-is."""

    def __init__(self, kind, title, intro=None, rows=None, outro=None, lines=None):
        self.kind = kind
        self.title = title
        self.intro = intro or []
        self.rows = rows or []
        self.outro = outro or []
        self.lines = lines or []


class Doc:
    def __init__(self, preamble, sections, warnings=None):
        self.preamble = preamble
        self.sections = sections
        self.warnings = warnings or []

    def section(self, kind, create=False):
        for s in self.sections:
            if s.kind == kind:
                return s
        if not create:
            return None
        if kind == "log":
            s = Section("log", LOG_TITLE)
            self.sections.append(s)
        else:
            s = Section(kind, SECTION_TITLES[kind])
            order = ["open", "proposed", "done"]
            pos = len(self.sections)
            for i, other in enumerate(self.sections):
                if other.kind == "log" or (other.kind in order and order.index(other.kind) > order.index(kind)):
                    pos = i
                    break
            self.sections.insert(pos, s)
        return s

    def rows(self, kind):
        s = self.section(kind)
        return s.rows if s else []

    def all_rows(self):
        for kind in ("open", "proposed", "done"):
            for row in self.rows(kind):
                yield kind, row

    def find(self, task_id):
        for kind in ("open", "proposed", "done"):
            for i, row in enumerate(self.rows(kind)):
                if row["id"] == task_id:
                    return kind, i, row
        return None, None, None

    def next_id(self):
        highest = 0
        for _, row in self.all_rows():
            m = ID_RE.match(row["id"])
            if m:
                highest = max(highest, int(m.group(1)))
        log = self.section("log")
        for line in log.lines if log else []:
            for n in re.findall(r"\bT-(\d{3,})\b", line):
                highest = max(highest, int(n))
        return f"T-{highest + 1:03d}"

    @property
    def last_sweep(self):
        for line in self.preamble:
            m = LAST_SWEEP_RE.match(line)
            if m:
                return m.group(1).strip()
        return ""

    @last_sweep.setter
    def last_sweep(self, value):
        for i, line in enumerate(self.preamble):
            if LAST_SWEEP_RE.match(line):
                self.preamble[i] = f"Last sweep: {value}"
                return
        for i, line in enumerate(self.preamble):
            if line.strip() == MARKER:
                self.preamble.insert(i + 1, f"Last sweep: {value}")
                return
        self.preamble.append(f"Last sweep: {value}")

    def log(self, line):
        self.section("log", create=True).lines.append(f"- {line}")


def escape_cell(value):
    text = "" if value is None else str(value)
    text = re.sub(r"\s*[\r\n]+\s*", " ", text).strip()
    return text.replace("|", "\\|")


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, buf, i = [], [], 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            buf.append("|")
            i += 2
            continue
        if s[i] == "|":
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(s[i])
        i += 1
    cells.append("".join(buf).strip())
    return cells


def _trim(lines):
    lines = list(lines)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def _kind_for(title):
    t = title.strip().lower()
    if t == "open":
        return "open"
    if t.startswith("proposed"):
        return "proposed"
    if t == "done":
        return "done"
    if t == LOG_TITLE.lower():
        return "log"
    return "other"


def _parse_task_section(kind, title, body, first_line_no, warnings):
    start = next((i for i, line in enumerate(body) if line.lstrip().startswith("|")), None)
    if start is None:
        return Section(kind, title, intro=_trim(body))
    end = start
    while end < len(body) and body[end].lstrip().startswith("|"):
        end += 1
    table = body[start:end]
    header = [c.lower() for c in split_row(table[0])]
    if header != [c.lower() for c in COLUMNS]:
        raise ParseError(f"line {first_line_no + start}: the '{title}' table must have the columns "
                         f"| {' | '.join(COLUMNS)} |")
    if len(table) < 2 or not SEPARATOR_RE.match(table[1].strip()):
        raise ParseError(f"line {first_line_no + start + 1}: missing |---| separator row under the '{title}' header")
    rows = []
    for offset, line in enumerate(table[2:], start=start + 2):
        cells = split_row(line)
        if len(cells) > len(COLUMNS):
            raise ParseError(f"line {first_line_no + offset}: {len(cells)} cells instead of {len(COLUMNS)}; "
                             "write a | inside a cell as \\|")
        if len(cells) < len(COLUMNS):
            warnings.append(f"line {first_line_no + offset}: only {len(cells)} cells, the rest were left blank")
            cells += [""] * (len(COLUMNS) - len(cells))
        if not any(cells):
            continue
        rows.append(dict(zip(FIELDS, cells)))
    for offset in [i for i in range(start) if LOOSE_ROW_RE.match(body[i])] + \
                  [i for i in range(end, len(body)) if LOOSE_ROW_RE.match(body[i])]:
        warnings.append(f"line {first_line_no + offset}: looks like a table row but is not parsed (only rows "
                        f"directly under the '{title}' header with a leading | are read); move it into the table")
    return Section(kind, title, intro=_trim(body[:start]), rows=rows, outro=_trim(body[end:]))


def parse(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    lines = [line.rstrip() for line in text.split("\n")]
    heads = [i for i, line in enumerate(lines) if line.startswith("## ")]
    preamble = _trim(lines[: heads[0]] if heads else lines)
    sections, warnings, seen = [], [], set()
    for n, h in enumerate(heads):
        title = lines[h][3:].strip()
        body = lines[h + 1: heads[n + 1] if n + 1 < len(heads) else len(lines)]
        kind = _kind_for(title)
        if kind in seen and kind != "other":
            raise ParseError(f"line {h + 1}: a second '## {title}' section; merge it into the first one")
        seen.add(kind)
        if kind in SECTION_TITLES:
            sections.append(_parse_task_section(kind, title, body, h + 2, warnings))
        else:
            if kind == "other" and any(LOOSE_ROW_RE.match(line) for line in body):
                names = ", ".join(f"'## {t}'" for t in list(SECTION_TITLES.values()) + [LOG_TITLE])
                warnings.append(f"line {h + 1}: '## {title}' is not a section the tracker reads ({names}), "
                                "so its table rows are ignored; rename the heading or move the rows")
            sections.append(Section(kind, title, lines=_trim(body)))
    return Doc(preamble, sections, warnings)


def _row_line(row):
    return "| " + " | ".join(escape_cell(row.get(f, "")) for f in FIELDS) + " |"


def serialise(doc):
    out = []
    if doc.preamble:
        out += doc.preamble + [""]
    for s in doc.sections:
        out += [f"## {s.title}", ""]
        if s.kind in SECTION_TITLES:
            if s.intro:
                out += s.intro + [""]
            out.append("| " + " | ".join(COLUMNS) + " |")
            out.append("|" + "---|" * len(COLUMNS))
            out += [_row_line(r) for r in s.rows]
            if s.outro:
                out += [""] + s.outro
            out.append("")
        elif s.lines:
            out += s.lines + [""]
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def revision(doc):
    """Fingerprint of the task rows only: Last sweep, the change log and prose do not change it."""
    lines = [f"{kind}\t{_row_line(row)}" for kind, row in doc.all_rows()]
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()[:12]


def duplicate_ids(doc):
    seen, dups = set(), []
    for _, row in doc.all_rows():
        if row["id"] in seen and row["id"] not in dups:
            dups.append(row["id"])
        seen.add(row["id"])
    return dups


def is_date(value):
    if not isinstance(value, str) or not DATE_RE.match(value):
        return False
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def is_unassigned(owner):
    return (owner or "").strip().lower() in ("", "unassigned", "tbc", "?")


def done_date(row):
    m = DONE_NOTE_RE.search(row.get("notes", ""))
    return m.group(1) if m and is_date(m.group(1)) else ""


def validate(doc):
    errors, warnings = [], list(doc.warnings)
    if MARKER not in doc.preamble:
        warnings.append(f"the header has no {MARKER} line")
    for kind in SECTION_TITLES:
        if doc.section(kind) is None:
            warnings.append(f"no '## {SECTION_TITLES[kind]}' section")
    seen = {}
    for kind, row in doc.all_rows():
        rid = row["id"] or "(no ID)"
        if not ID_RE.match(row["id"]):
            errors.append(f"{rid}: ID should look like T-001")
        if row["id"] in seen:
            errors.append(f"{rid}: duplicate ID (in {seen[row['id']]} and {SECTION_TITLES[kind]})")
        seen[row["id"]] = SECTION_TITLES[kind]
        if not row["action"]:
            errors.append(f"{rid}: no action text")
        if row["status"] not in SECTION_STATUSES[kind]:
            errors.append(f"{rid}: status '{row['status']}' is not allowed in '{SECTION_TITLES[kind]}' "
                          f"(use {', '.join(SECTION_STATUSES[kind])})")
        for f in ("raised", "due"):
            if row[f] and not is_date(row[f]):
                errors.append(f"{rid}: {f} date '{row[f]}' is not a real YYYY-MM-DD date")
        if kind == "open" and is_unassigned(row["owner"]):
            warnings.append(f"{rid}: unassigned (no owner)")
        if kind == "done" and not done_date(row):
            warnings.append(f"{rid}: no 'done YYYY-MM-DD' in Notes")
    return errors, warnings


def load(path):
    return parse(Path(path).read_text(encoding="utf-8"))


def backup_file(path):
    """Copy path into .task-tracker-backups/ with a timestamp and keep only the newest BACKUPS_KEPT."""
    path = Path(path)
    folder = path.parent / BACKUP_DIR
    folder.mkdir(exist_ok=True)
    when = dt.datetime.now()
    dest = folder / f"{path.name}.{when:%Y%m%d-%H%M%S-%f}.bak"
    while dest.exists():
        when += dt.timedelta(microseconds=1)
        dest = folder / f"{path.name}.{when:%Y%m%d-%H%M%S-%f}.bak"
    shutil.copyfile(path, dest)
    old = sorted(folder.glob(f"{path.name}.*.bak"))
    for extra in old[:-BACKUPS_KEPT]:
        extra.unlink()
    return dest


def write_atomic(path, text, backup=True):
    """Write via a fsynced temporary file next to the real file, then rename it into place.

    A symlinked path is followed so the link stays a link, and the file keeps its permissions.
    Returns the backup path, or None when no backup was made.
    """
    path = Path(path)
    target = Path(os.path.realpath(path))
    saved = backup_file(path) if backup and target.exists() else None
    if target.exists():
        mode = stat.S_IMODE(target.stat().st_mode)
    else:
        umask = os.umask(0)
        os.umask(umask)
        mode = 0o666 & ~umask
    fd, tmp = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.chmod(tmp, mode)
        os.replace(tmp, target)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    try:
        dir_fd = os.open(str(target.parent), os.O_RDONLY)
    except OSError:
        return saved
    try:
        os.fsync(dir_fd)
    except OSError:
        pass
    finally:
        os.close(dir_fd)
    return saved


def as_json(doc):
    return {
        "revision": revision(doc),
        "last_sweep": doc.last_sweep,
        "next_id": doc.next_id(),
        **{kind: doc.rows(kind) for kind in SECTION_TITLES},
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read, check and tidy TASKS.md")
    ap.add_argument("command", choices=["init", "validate", "revision", "show", "normalise"])
    ap.add_argument("--tasks", default="TASKS.md", help="path to TASKS.md")
    args = ap.parse_args(argv)
    path = Path(args.tasks)

    if args.command == "init":
        if path.exists():
            print(json.dumps({"created": False, "path": str(path.resolve()), "reason": "already exists, left unchanged"}))
            return 0
        path.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(path, TEMPLATE, backup=False)
        print(json.dumps({"created": True, "path": str(path.resolve()), "revision": revision(parse(TEMPLATE))}))
        return 0

    if not path.exists():
        print(f"{path} not found. Run: tasks_md.py init --tasks {path}", file=sys.stderr)
        return 1
    try:
        doc = load(path)
    except (ParseError, OSError, UnicodeDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, indent=2))
        return 1

    if args.command == "revision":
        print(revision(doc))
    elif args.command == "show":
        print(json.dumps(as_json(doc), indent=2, ensure_ascii=False))
    elif args.command == "validate":
        errors, warnings = validate(doc)
        print(json.dumps({"ok": not errors, "revision": revision(doc), "errors": errors, "warnings": warnings},
                         indent=2, ensure_ascii=False))
        return 1 if errors else 0
    elif args.command == "normalise":
        text = serialise(doc)
        changed = text != path.read_text(encoding="utf-8")
        saved = write_atomic(path, text) if changed else None
        print(json.dumps({"changed": changed, "revision": revision(doc), "backup": str(saved) if saved else None}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
