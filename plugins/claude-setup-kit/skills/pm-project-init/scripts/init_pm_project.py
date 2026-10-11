#!/usr/bin/env python3
"""Create a ready-to-use project management folder for working with Claude.

Creates <root>/<slug-of-name>/ with phase folders, inputs/outputs/archive,
a filled-in CLAUDE.md and starter context files. Never overwrites: existing
files are skipped and reported, existing folders are reused.

Python 3 standard library only. By Benjamin Vermeulen, @SIwithBen. MIT licence.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

TO_CONFIRM = "[to confirm]"

FOLDERS = [
    "01-initiation",
    "02-planning",
    "03-execution",
    "04-monitoring-and-control",
    "05-closure",
    "context",
    "inputs",
    "outputs",
    "archive",
]

TEMPLATE_PATH = Path(__file__).resolve().parents[3] / "templates" / "folder-CLAUDE.md"

FALLBACK_TEMPLATE = """# [Project name]

This is the working folder for [Project name]. Read this file before you start any task here.

## Project at a glance
- Sponsor: [Sponsor]
- Project manager: [Project manager]
- Dates: [Start date] to [End date]
- Goal: [Goal]
- Key stakeholders: [Key stakeholders]

## Folder map
- `context/` holds the project brief, stakeholders, glossary and decisions log.
- `01-initiation/` to `05-closure/` hold the documents for each project phase.
- `inputs/` holds raw notes and transcripts; `outputs/` holds drafts you produce; ignore `archive/`.

## Client terminology
[Terminology]

## Reporting rules
[Reporting rules]

## How to work here
- Never invent figures, dates, names or owners. Write "[to confirm]" for anything you cannot find.
- Save new drafts in `outputs/`; never overwrite or delete an existing file without asking first.
"""


def slugify(name):
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-")


def validate_name(name):
    """Return an error message, or None if the name is safe to use."""
    if not name or not name.strip():
        return "Project name is empty."
    if any(c in name for c in ("/", "\\", "\x00")) or ".." in name:
        return "Project name must not contain '/', '\\' or '..'."
    if not slugify(name):
        return "Project name has no letters or digits to build a folder name from."
    return None


def value(text):
    text = (text or "").strip()
    return text if text else TO_CONFIRM


def split_list(text):
    return [part.strip() for part in re.split(r"[;\n]", text or "") if part.strip()]


def bullets(text):
    items = split_list(text)
    return "\n".join(f"- {item}" for item in items) if items else f"- {TO_CONFIRM}"


def load_template():
    if TEMPLATE_PATH.is_file():
        lines = TEMPLATE_PATH.read_text(encoding="utf-8").splitlines()
        if lines and lines[0].startswith("> Where this goes"):
            lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
        return "\n".join(lines) + "\n"
    return FALLBACK_TEMPLATE


def build_claude_md(args):
    stakeholders = split_list(args.stakeholders)
    replacements = {
        "[Project name]": args.name.strip(),
        "[Sponsor]": value(args.sponsor),
        "[Project manager]": value(args.pm),
        "[Start date]": value(args.start),
        "[End date]": value(args.end),
        "[Goal]": value(args.goal),
        "[Key stakeholders]": "; ".join(stakeholders) if stakeholders else TO_CONFIRM,
        "[Terminology]": bullets(args.terminology),
        "[Reporting rules]": bullets(args.reporting),
    }
    text = load_template()
    for token, replacement in replacements.items():
        text = text.replace(token, replacement)
    return text


def build_brief(args):
    return f"""# Project brief: {args.name.strip()}

| Item | Detail |
|---|---|
| Sponsor | {value(args.sponsor)} |
| Project manager | {value(args.pm)} |
| Start date | {value(args.start)} |
| End date | {value(args.end)} |
| Goal | {value(args.goal)} |

## Background
{TO_CONFIRM}

## Scope
**In scope:** {TO_CONFIRM}
**Out of scope:** {TO_CONFIRM}

## Key milestones
| Milestone | Target date |
|---|---|
| {TO_CONFIRM} | {TO_CONFIRM} |

## Budget
{TO_CONFIRM}
"""


def build_stakeholders(args):
    rows = []
    for item in split_list(args.stakeholders):
        match = re.fullmatch(r"(.+?)\s*\((.+)\)", item)
        name, role = (match.group(1), match.group(2)) if match else (item, TO_CONFIRM)
        rows.append(f"| {name} | {role} | {TO_CONFIRM} | {TO_CONFIRM} |")
    if not rows:
        rows.append(f"| {TO_CONFIRM} | {TO_CONFIRM} | {TO_CONFIRM} | {TO_CONFIRM} |")
    return (
        f"# Stakeholders: {args.name.strip()}\n\n"
        "| Stakeholder | Role / interest | Influence (H/M/L) | How to keep them informed |\n"
        "|---|---|---|---|\n" + "\n".join(rows) + "\n"
    )


def build_glossary(args):
    rows = [f"| {item} | |" for item in split_list(args.terminology)]
    if not rows:
        rows.append(f"| {TO_CONFIRM} | |")
    return (
        f"# Glossary: {args.name.strip()}\n\n"
        "Client terms, acronyms and words to avoid. Claude should use the client's words.\n\n"
        "| Term | Meaning / use instead |\n"
        "|---|---|\n" + "\n".join(rows) + "\n"
    )


def build_decisions(args):
    return (
        f"# Decisions log: {args.name.strip()}\n\n"
        "Add one line per decision. Newest at the bottom.\n\n"
        "| Date | Decision | Made by | Reason | Link / source |\n"
        "|---|---|---|---|---|\n"
    )


INPUTS_README = """# inputs

Raw material for this project: meeting notes, transcripts, emails, exports.
Claude reads from here and does not edit these files.
"""

OUTPUTS_README = """# outputs

Drafts Claude produces for this project. Review every draft before it goes to anyone.
Suggested file names: YYYY-MM-DD_short-name_v0.1.md
"""


def plan_files(args):
    return {
        "CLAUDE.md": build_claude_md(args),
        "context/project-brief.md": build_brief(args),
        "context/stakeholders.md": build_stakeholders(args),
        "context/glossary.md": build_glossary(args),
        "context/decisions-log.md": build_decisions(args),
        "inputs/README.md": INPUTS_README,
        "outputs/README.md": OUTPUTS_README,
    }


def run(args):
    report = {
        "project_name": args.name.strip(),
        "slug": slugify(args.name),
        "dry_run": args.dry_run,
        "created": [],
        "skipped": [],
        "reused": [],
        "errors": [],
    }
    root = Path(args.root).expanduser().resolve()
    project = root / report["slug"]
    report["project_dir"] = str(project)

    if project.exists() and not project.is_dir():
        report["errors"].append(f"{project} exists and is not a folder; nothing was created.")
        return report

    targets = [("", project)] + [(f"{f}/", project / f) for f in FOLDERS]
    for label, path in targets:
        label = label or f"{report['slug']}/"
        if path.is_dir():
            report["reused"].append(label)
        elif path.exists():
            report["errors"].append(f"{label} exists and is not a folder; skipped.")
        else:
            if not args.dry_run:
                path.mkdir(parents=True)
            report["created"].append(label)

    for rel, content in plan_files(args).items():
        path = project / rel
        if path.exists():
            report["skipped"].append(rel)
            continue
        if not path.parent.is_dir():
            if not args.dry_run:
                report["errors"].append(f"{rel}: parent folder missing; skipped.")
                continue
        if not args.dry_run:
            try:
                with open(path, "x", encoding="utf-8") as handle:
                    handle.write(content)
            except FileExistsError:
                report["skipped"].append(rel)
                continue
        report["created"].append(rel)
    return report


def print_report(report):
    prefix = "Would create" if report["dry_run"] else "Created"
    print(f"Project folder: {report['project_dir']}" + ("  (dry run, nothing written)" if report["dry_run"] else ""))
    sections = [
        (prefix, report["created"]),
        ("Skipped (already exists, left unchanged)", report["skipped"]),
        ("Reused existing folders", report["reused"]),
        ("Problems", report["errors"]),
    ]
    for title, items in sections:
        print(f"\n{title}: {len(items)}")
        for item in items:
            print(f"  - {item}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Create a PM project folder for working with Claude. Never overwrites existing files.")
    parser.add_argument("--root", default=".", help="Parent folder, e.g. your main 'PM Projects' folder (default: current folder).")
    parser.add_argument("--name", required=True, help="Project name; the folder name is a slug of it.")
    parser.add_argument("--sponsor", default="")
    parser.add_argument("--pm", default="", help="Project manager.")
    parser.add_argument("--start", default="", help="Start date.")
    parser.add_argument("--end", default="", help="End date.")
    parser.add_argument("--goal", default="")
    parser.add_argument("--stakeholders", default="", help="Semicolon-separated, e.g. 'Ana Lopez (Finance lead); IT steering group'.")
    parser.add_argument("--terminology", default="", help="Semicolon-separated client terms and rules.")
    parser.add_argument("--reporting", default="", help="Semicolon-separated reporting rules.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing anything.")
    parser.add_argument("--json", action="store_true", help="Print the report as JSON.")
    args = parser.parse_args(argv)

    error = validate_name(args.name)
    if error:
        if args.json:
            print(json.dumps({"error": error}))
        else:
            print(f"Error: {error}", file=sys.stderr)
        return 2

    report = run(args)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
