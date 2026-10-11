#!/usr/bin/env python3
"""Make a Gantt chart (HTML, Excel and PowerPoint) from a task list in JSON, CSV or Excel.

Usage:
  python3 gantt.py --input plan.csv --out-dir outputs --name "Website relaunch" [--formats html,xlsx,pptx]
                   [--day-mode calendar|working] [--date-format auto|iso|dmy|mdy] [--today YYYY-MM-DD]

Writes <slug>-gantt.html/.xlsx/.pptx and prints a JSON summary. Writes local files only; never sends or uploads.
Exit codes: 0 done (check the summary for gaps), 2 input needs a decision or a fix.

By Benjamin Vermeulen, @SIwithBen. MIT licence.
"""
import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gantt_core import DATE_FORMATS, DAY_MODES, InputError, load_plan, summary  # noqa: E402

FORMATS = ("html", "xlsx", "pptx")


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "plan"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Make a Gantt chart from a task list.")
    ap.add_argument("--input", required=True, help="Task list: .json, .csv or .xlsx")
    ap.add_argument("--out-dir", default=".", help="Folder for the output files (created if missing)")
    ap.add_argument("--name", help="Plan name, used for titles and file names (default: input file name)")
    ap.add_argument("--formats", default="html,xlsx,pptx", help="Comma list of html, xlsx, pptx")
    ap.add_argument("--day-mode", choices=DAY_MODES, default="calendar", help="Count durations in calendar or working days")
    ap.add_argument("--date-format", choices=DATE_FORMATS, default="auto", help="How to read slash dates (default auto: DD/MM/YYYY)")
    ap.add_argument("--today", help="Override today's date (YYYY-MM-DD), for tests and snapshots")
    args = ap.parse_args(argv)

    formats = [f.strip().lower() for f in args.formats.split(",") if f.strip()]
    bad = [f for f in formats if f not in FORMATS]
    if bad or not formats:
        print(json.dumps({"error": f"Unknown format(s): {', '.join(bad) or 'none given'}. Use html, xlsx, pptx."}))
        return 2
    try:
        today = dt.date.fromisoformat(args.today) if args.today else None
    except ValueError:
        print(json.dumps({"error": f"--today must be YYYY-MM-DD, got {args.today}."}))
        return 2

    try:
        plan = load_plan(args.input, name=args.name, today=today, day_mode=args.day_mode, date_format=args.date_format)
    except (InputError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}))
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = out_dir / f"{slugify(plan['name'])}-gantt"
    files, errors = [], []
    for fmt in formats:
        path = base.with_suffix(f".{fmt}")
        try:
            if fmt == "html":
                from render_html import render_html
                render_html(plan, path)
            elif fmt == "xlsx":
                from render_xlsx import render_xlsx
                render_xlsx(plan, path)
            else:
                from render_pptx import render_pptx
                render_pptx(plan, path)
            files.append(path)
        except ImportError as exc:
            pkg = "openpyxl" if fmt == "xlsx" else "python-pptx"
            errors.append(f"{fmt}: skipped, needs {pkg} (pip install {pkg}): {exc}")
    out = summary(plan, files)
    if errors:
        out["errors"] = errors
    print(json.dumps(out, indent=2))
    return 0 if files else 2


if __name__ == "__main__":
    sys.exit(main())
