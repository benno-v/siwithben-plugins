#!/usr/bin/env python3
"""Apply a task-tracker-changes block (from the dashboard or a sweep) to TASKS.md.

Python 3 standard library only.

  apply_changes.py --tasks TASKS.md --changes tasks-changes.json [--dry-run] [--force] [--proposed-only]
  apply_changes.py --tasks TASKS.md --changes - < pasted.txt

--changes accepts the fenced ```task-tracker-changes block (with any text around it) or raw JSON.
The revision only covers the task rows, so a new Last sweep line or change log entry never blocks a block.
Ops that carry a 'before' snapshot (the dashboard adds one) are checked against the row as it is now:
complete, approve and reject need the row unchanged; update skips only the fields changed since.
If base_revision no longer matches TASKS.md, ops on existing rows without a snapshot refuse the whole
block unless --force; adds always go ahead, subject to the duplicate check.
--proposed-only (scheduled sweeps) only adds rows to "Proposed, needs approval" and updates Last sweep.
Nothing is written if TASKS.md has duplicate IDs, or if it changed while the changes were being applied.
Prints a JSON summary. Exit codes: 0 done (some ops may be skipped), 1 bad input, 2 refused.
"""
import argparse
import copy
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tasks_md as tm  # noqa: E402

FENCE_RE = re.compile(r"```task-tracker-changes[ \t]*\n(.*?)\n?```", re.S)
EDITABLE = {"action", "owner", "source", "raised", "due", "status", "notes"}
OPS = ("update", "complete", "approve", "reject", "add")
NOW_RE = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")
REJECT_LOG_RE = re.compile(r"^- .*?: reject (T-\d{3,}) \((.*)\) \[block [0-9a-f]{8}\]$")


class InputError(ValueError):
    pass


def extract_block(text):
    blocks = FENCE_RE.findall(text)
    if len(blocks) > 1:
        raise InputError("found more than one task-tracker-changes block; apply them one at a time")
    payload = blocks[0] if blocks else text.strip()
    if payload.startswith("```"):
        payload = re.sub(r"^```[a-z-]*\s*\n|\n?```\s*$", "", payload)
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise InputError(f"no task-tracker-changes block or valid JSON found ({exc.msg}, line {exc.lineno})")
    if not isinstance(data, dict) or not isinstance(data.get("ops"), list):
        raise InputError("the changes must be a JSON object with an 'ops' list")
    if not isinstance(data.get("base_revision"), str) or not re.fullmatch(r"[0-9a-f]{12}", data["base_revision"]):
        raise InputError("base_revision is missing or is not 12 hex characters")
    return data


def _clean_fields(fields, kind):
    """Return (clean fields, error). kind is the section the row will end up in."""
    if not isinstance(fields, dict):
        return None, "fields must be a JSON object"
    if not fields:
        return None, "no fields given"
    unknown = sorted(set(fields) - EDITABLE)
    if unknown:
        return None, f"unknown field(s): {', '.join(unknown)}"
    clean = {}
    for key, value in fields.items():
        if value is None:
            value = ""
        if not isinstance(value, str):
            return None, f"{key} must be text"
        value = re.sub(r"\s+", " ", value).strip()
        if key in ("raised", "due") and value and not tm.is_date(value):
            return None, f"{key} '{value}' is not a real YYYY-MM-DD date"
        if key == "owner" and value.lower() == "unassigned":
            value = ""
        if key == "action" and not value:
            return None, "action text cannot be empty"
        if key == "status" and value not in tm.SECTION_STATUSES[kind]:
            hint = "; use the complete op to mark a task done" if value == "Done" else ""
            return None, f"status '{value}' is not allowed in '{tm.SECTION_TITLES[kind]}'{hint}"
        clean[key] = value
    return clean, None


def block_id(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode("utf-8")).hexdigest()[:8]


def _norm(text):
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def _ws(text):
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def _owner_key(owner):
    return "" if tm.is_unassigned(owner) else _norm(owner)


def _text(value):
    return "" if value is None else str(value)


def changed_rows(doc, ops):
    """For ops carrying a 'before' snapshot, describe how the target row differs now."""
    report = []
    for op in ops:
        if not isinstance(op, dict) or not isinstance(op.get("before"), dict) or not isinstance(op.get("id"), str):
            continue
        kind, _, row = doc.find(op["id"])
        before = op["before"]
        if row is None:
            report.append({"id": op["id"], "change": "no longer in TASKS.md"})
            continue
        diffs = []
        if before.get("section") and before["section"] != kind:
            diffs.append(f"moved from {before['section']} to {kind}")
        for f in tm.FIELDS[1:]:
            if f in before and _text(before[f]) != row[f]:
                diffs.append(f"{f}: '{_text(before[f])}' -> '{row[f]}'")
        if diffs:
            report.append({"id": op["id"], "change": "; ".join(diffs)})
    return report


def snapshot_checks(doc, ops, mismatch, force):
    """Check each op's 'before' snapshot against doc as it was read, before any op runs.

    Returns (checks, unguarded). checks maps an op index to ("skip", reason) or ("drop", {field: reason});
    unguarded lists the indexes of ops on existing rows that have no snapshot while the revision differs.
    """
    checks, unguarded = {}, []
    for i, op in enumerate(ops):
        if not isinstance(op, dict) or op.get("op") not in OPS or op["op"] == "add" or not isinstance(op.get("id"), str):
            continue
        kind, _, row = doc.find(op["id"])
        if row is None:
            continue
        before = op.get("before")
        if before is None:
            if mismatch:
                unguarded.append(i)
            continue
        if not isinstance(before, dict):
            checks[i] = ("skip", "'before' must be a JSON object")
            continue
        if before.get("section") and before["section"] != kind:
            checks[i] = ("skip", f"moved from {before['section']} to {kind} since the block was made")
            continue
        diffs = {f: f"{f} changed since the block was made ('{_text(before[f])}' -> '{row[f]}')"
                 for f in tm.FIELDS[1:] if f in before and _text(before[f]) != row[f]}
        if op["op"] == "update":
            fields = op.get("fields") if isinstance(op.get("fields"), dict) else {}
            drop = {f: diffs[f] for f in fields if f in diffs}
            if mismatch and not force:
                for f in fields:
                    if f in EDITABLE and f not in before:
                        drop.setdefault(f, f"{f} has no before snapshot and TASKS.md changed since the block was made")
            if drop:
                checks[i] = ("drop", drop)
        else:
            # complete / approve / reject only need the row to still mean the same task:
            # an extra source reference or a note added by a sweep does not block a tick.
            core = {f: d for f, d in diffs.items() if f in CORE_FIELDS}
            if core:
                checks[i] = ("skip", "row changed since the block was made: " + "; ".join(core.values()))
    return checks, unguarded


CORE_FIELDS = ("action", "owner", "due", "status")


def rejected_actions(doc):
    """(id, logged detail) for every proposed row rejected in the change log."""
    log = doc.section("log")
    found = []
    for line in log.lines if log else []:
        m = REJECT_LOG_RE.match(line.strip())
        if m:
            found.append((m.group(1), m.group(2)))
    return found


def find_duplicate(doc, clean, extended):
    """Reason an add duplicates an existing or rejected task, or None.

    extended (sweeps) also checks Done rows and actions rejected in the change log.
    """
    action, owner = _norm(clean["action"]), _owner_key(clean.get("owner", ""))
    for kind, r in doc.all_rows():
        if (extended or kind != "done") and _norm(r["action"]) == action and _owner_key(r["owner"]) == owner:
            if kind == "done":
                return f"already done as {r['id']} (same action and owner)"
            return f"looks like a duplicate of {r['id']} (same action and owner)"
    if extended:
        ws = _ws(clean["action"])
        for rid, detail in rejected_actions(doc):
            if _norm(detail) == action or _ws(detail).startswith(ws + "; "):
                return f"same action as {rid}, which was rejected before (see the change log)"
    return None


def apply_ops(doc, data, today, now, proposed_only=False, checks=None):
    """Apply ops to doc in place. Returns (applied, skipped)."""
    source = data.get("source") if re.fullmatch(r"[a-z][a-z-]{0,20}", str(data.get("source", ""))) else "dashboard"
    tag = f"[block {block_id(data)}]"
    checks = checks or {}
    applied, skipped = [], []

    def skip(i, op, reason, field=None):
        entry = {"index": i, "op": op.get("op") if isinstance(op, dict) else None,
                 "id": op.get("id") if isinstance(op, dict) else None, "reason": reason}
        if field:
            entry["field"] = field
        skipped.append(entry)

    def done(i, name, tid, detail=""):
        applied.append({"index": i, "op": name, "id": tid, "detail": detail})
        doc.log(f"{now} {source}: {name} {tid}{' (' + detail + ')' if detail else ''} {tag}")

    for i, op in enumerate(data["ops"]):
        if not isinstance(op, dict) or op.get("op") not in OPS:
            skip(i, op if isinstance(op, dict) else {}, f"unknown op; use one of {', '.join(OPS)}")
            continue
        name = op["op"]
        if proposed_only and name != "add":
            skip(i, op, "proposed-only mode: only new proposed rows can be added")
            continue
        check = checks.get(i)
        if check and check[0] == "skip":
            skip(i, op, check[1])
            continue

        if name == "add":
            if not isinstance(op.get("fields"), dict):
                skip(i, op, "add needs fields as a JSON object")
                continue
            fields = dict(op["fields"])
            status = fields.get("status") or ("Proposed" if proposed_only else "Open")
            note = ""
            if proposed_only and status != "Proposed":
                status, note = "Proposed", "added to Proposed (proposed-only mode)"
            kind = "proposed" if status == "Proposed" else "open"
            fields["status"] = status
            if "action" not in fields:
                skip(i, op, "add needs an action")
                continue
            clean, err = _clean_fields(fields, kind)
            if err:
                skip(i, op, err)
                continue
            dup = find_duplicate(doc, clean, extended=source != "dashboard")
            if dup:
                skip(i, op, dup)
                continue
            row = {f: "" for f in tm.FIELDS}
            row.update(clean)
            row["id"] = doc.next_id()
            row["raised"] = row["raised"] or today
            row["source"] = row["source"] or f"{source}: added ({today})"
            doc.section(kind, create=True).rows.append(row)
            done(i, "add", row["id"], note or clean["action"])
            continue

        tid = op.get("id")
        kind, idx, row = doc.find(tid) if isinstance(tid, str) else (None, None, None)
        if row is None:
            skip(i, op, f"unknown id {tid!r}")
            continue

        if name == "complete":
            if kind == "done":
                skip(i, op, "already done")
                continue
            if kind == "proposed":
                skip(i, op, "still proposed; approve it first")
                continue
            when = op.get("date") or today
            if not tm.is_date(when):
                skip(i, op, f"date '{when}' is not a real YYYY-MM-DD date")
                continue
            doc.section("open").rows.pop(idx)
            row["status"] = "Done"
            row["notes"] = f"{row['notes']}; done {when}" if row["notes"] else f"done {when}"
            doc.section("done", create=True).rows.insert(0, row)
            done(i, "complete", tid)

        elif name == "update":
            fields = op.get("fields")
            if check and check[0] == "drop" and isinstance(fields, dict):
                for f, reason in check[1].items():
                    skip(i, op, reason, field=f)
                fields = {k: v for k, v in fields.items() if k not in check[1]}
                if not fields:
                    continue
            clean, err = _clean_fields(fields, kind)
            if err:
                skip(i, op, err)
                continue
            changes = {k: v for k, v in clean.items() if row[k] != v}
            if not changes:
                skip(i, op, "no change")
                continue
            row.update(changes)
            done(i, "update", tid, ", ".join(f"{k} {v or 'blank'}" if k in ("owner", "due", "status", "raised")
                                            else f"{k} edited" for k, v in changes.items()))

        elif name == "approve":
            if kind != "proposed":
                skip(i, op, "already approved" if kind == "open" else f"not in '{tm.SECTION_TITLES['proposed']}'")
                continue
            clean = {}
            if op.get("fields") not in (None, {}):
                clean, err = _clean_fields(op["fields"], "open")
                if err:
                    skip(i, op, err)
                    continue
            doc.section("proposed").rows.pop(idx)
            row.update(clean)
            if row["status"] not in tm.OPEN_STATUSES:
                row["status"] = "Open"
            doc.section("open", create=True).rows.append(row)
            done(i, "approve", tid, "no owner yet" if tm.is_unassigned(row["owner"]) else "")

        elif name == "reject":
            if kind != "proposed":
                skip(i, op, f"only proposed tasks can be rejected; {tid} is in '{tm.SECTION_TITLES[kind]}'")
                continue
            doc.section("proposed").rows.pop(idx)
            reason = re.sub(r"\s+", " ", str(op.get("reason") or "")).strip()
            done(i, "reject", tid, row["action"] + (f"; {reason}" if reason else ""))
    return applied, skipped


def run(tasks_path, changes_text, dry_run=False, force=False, proposed_only=False, today=None, now=None):
    """Returns (exit code, summary dict)."""
    summary = {"status": None, "dry_run": dry_run, "applied": [], "skipped": [], "messages": []}
    today = today or dt.date.today().isoformat()
    now = now or dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not tm.is_date(today):
        summary.update(status="error", messages=[f"--today '{today}' is not a real YYYY-MM-DD date"])
        return 1, summary
    if not isinstance(now, str) or not NOW_RE.fullmatch(now) or not tm.is_date(now[:10]):
        summary.update(status="error", messages=[f"--now '{now}' is not a real YYYY-MM-DD HH:MM time"])
        return 1, summary
    try:
        data = extract_block(changes_text)
        original = Path(tasks_path).read_text(encoding="utf-8")
        doc = tm.parse(original)
    except (InputError, tm.ParseError, OSError, UnicodeDecodeError) as exc:
        summary.update(status="error", messages=[str(exc)])
        return 1, summary

    dups = tm.duplicate_ids(doc)
    if dups:
        summary.update(status="error", messages=[
            f"TASKS.md has duplicate IDs ({', '.join(dups)}), so changes could hit the wrong row. Nothing was "
            "written. Fix them first; tasks_md.py validate lists them."])
        return 1, summary

    current = tm.revision(doc)
    mismatch = data["base_revision"] != current
    summary.update(base_revision=data["base_revision"], current_revision=current)
    log = doc.section("log")
    tag = f"[block {block_id(data)}]"
    earlier = [line for line in (log.lines if log else []) if tag in line]
    if earlier:
        summary["messages"].append(f"This block was already applied (change log: {earlier[0][2:18]}). Nothing to do.")
        summary["status"] = "refused"
        return 2, summary

    checks, unguarded = snapshot_checks(doc, data["ops"], mismatch, force)
    if mismatch:
        summary["changed_since"] = changed_rows(doc, data["ops"])
        if unguarded and not force:
            listed = ", ".join(f"#{i} {data['ops'][i]['op']} {data['ops'][i]['id']}" for i in unguarded)
            summary["unguarded_ops"] = unguarded
            summary["messages"].append(
                f"TASKS.md has changed since these changes were made (revision {data['base_revision']}, now "
                f"{current}) and these ops have no before snapshot to check against: {listed}. Nothing was "
                "written. Rebuild the changes from the current TASKS.md, or check the rows and re-run with --force.")
            summary["status"] = "refused"
            return 2, summary
        summary["messages"].append(
            f"TASKS.md has changed since these changes were made (revision {data['base_revision']}, now {current}). "
            "Ops whose rows still match their before snapshot are applied; the rest are skipped with the reason.")
        if force and unguarded:
            summary["messages"].append("--force: ops without a before snapshot are applied too.")

    work = copy.deepcopy(doc)
    applied, skipped = apply_ops(work, data, today, now, proposed_only, checks)
    last_sweep = data.get("last_sweep")
    if last_sweep:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}( \d{2}:\d{2})?", str(last_sweep)) and tm.is_date(str(last_sweep)[:10]):
            work.last_sweep = last_sweep
        else:
            summary["messages"].append(f"last_sweep '{last_sweep}' ignored: use YYYY-MM-DD HH:MM")
            last_sweep = None
    errors, _ = tm.validate(work)
    summary.update(applied=applied, skipped=skipped, validation_errors=errors)
    changed = bool(applied) or bool(last_sweep)
    if dry_run:
        summary.update(status="dry-run", applied=[], would_apply=applied, new_revision=current,
                       would_be_revision=tm.revision(work))
        return 0, summary
    if not changed:
        summary.update(status="nothing to apply", new_revision=current)
        return 0, summary
    try:
        latest = Path(tasks_path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        latest = str(exc)
    if latest != original:
        summary.update(status="refused", applied=[], new_revision=current)
        summary["messages"].append("TASKS.md changed while these changes were being applied (a hand edit or another "
                                   "sweep). Nothing was written; run the same command again.")
        return 2, summary
    saved = tm.write_atomic(tasks_path, tm.serialise(work), backup=bool(applied))
    summary.update(status="applied", new_revision=tm.revision(work), backup=str(saved) if saved else None)
    return 0, summary


def main(argv=None):
    ap = argparse.ArgumentParser(description="Apply a task-tracker-changes block to TASKS.md")
    ap.add_argument("--tasks", default="TASKS.md")
    ap.add_argument("--changes", required=True, help="file with the block or JSON, or - for stdin")
    ap.add_argument("--dry-run", action="store_true", help="show what would happen, write nothing")
    ap.add_argument("--force", action="store_true",
                    help="TASKS.md changed since the block was made: also apply ops that have no before snapshot")
    ap.add_argument("--proposed-only", action="store_true", help="only add rows to Proposed (scheduled sweeps)")
    ap.add_argument("--today", help="YYYY-MM-DD, default today")
    ap.add_argument("--now", help="YYYY-MM-DD HH:MM for the change log, default now")
    args = ap.parse_args(argv)
    try:
        text = sys.stdin.read() if args.changes == "-" else Path(args.changes).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        code, summary = 1, {"status": "error", "dry_run": args.dry_run, "applied": [], "skipped": [],
                            "messages": [f"could not read the changes: {exc}"]}
    else:
        code, summary = run(args.tasks, text, args.dry_run, args.force, args.proposed_only, args.today, args.now)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
