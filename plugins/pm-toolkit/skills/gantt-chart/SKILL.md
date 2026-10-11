---
name: gantt-chart
description: Turn a task list into a Gantt chart as an interactive HTML page, an Excel workbook whose bars move when dates change, and a PowerPoint deck, with milestones, dependencies, the critical path and a list of gaps. Never invents dates or durations. Use when the user asks for a Gantt chart, a Gantt, a timeline or timeline view of a plan, a project schedule chart, or wants to see tasks, milestones or the critical path on a timeline.
---

# Gantt chart

Turn the user's tasks into a Gantt chart in three formats: an interactive HTML page, an Excel workbook and a PowerPoint deck. Anything that cannot be placed on the timeline from the user's own data is listed under "Unscheduled, needs dates", never guessed.

## Ground rules

- Work only from what the user gives you or what you can read. Never invent start dates, end dates, durations, owners or dependencies. A task without enough data is listed as unscheduled, not drawn.
- A task is drawn only when it has: a start and an end date; or a start (or end) date and a duration; or dependencies plus a duration, which fix its start (finish-to-start: it starts the day after its last dependency ends). A milestone needs one date or a dependency.
- Read only. When reading from a PM tool (Monday, Asana, Jira, Notion or similar), never create, edit, move or comment on anything there.
- Never send, share, upload or publish the chart. Save the files locally and tell the user where they are.
- If key inputs are missing, ask once, in one short numbered list, then continue with what you have.
- Plain British English, short sentences.

## Inputs to look for

1. **The tasks**, from one of:
   - a pasted list or table;
   - a CSV or Excel file (columns: `id, task, phase, owner, start, end, duration_days, depends_on, milestone, status, percent_complete`; other common names such as Assignee, Due date or Predecessors are understood);
   - a connected PM tool (Monday, Asana, Jira, Notion). Read the board, project or database only. Map its fields to the columns above, for example item or issue key to `id`, group or epic to `phase`, assignee to `owner`, timeline or start and due dates to `start` and `end`, and "blocked by" or dependency links to `depends_on`.
2. **Plan name**, used for titles and file names.
3. **Working days or calendar days?** Ask before assuming. If the user does not say, use calendar days and state that in your reply.
4. **Date format**, only if the dates use slashes and none of them settles it (every day is 12 or under). Ask whether they are DD/MM/YYYY or MM/DD/YYYY and pass `--date-format dmy` or `mdy`; the script refuses to guess. ISO dates (YYYY-MM-DD) are always safe.
5. **Where to save**. Default: the `outputs/` folder in the current working folder if there is one, otherwise the current folder.

## Method

1. **Collect** the tasks from the source above. Do not fill gaps: leave a missing date, duration, owner or dependency empty.
2. **Normalise** them to the task JSON schema and save it next to the outputs as `<plan-slug>-tasks.json` (CSV and Excel files can be passed to the script directly):

   ```json
   {
     "name": "Plan name",
     "tasks": [
       {"id": "T1", "task": "Kick-off workshop", "phase": "Initiation", "owner": "Project manager",
        "start": "2026-11-02", "end": "2026-11-03", "duration_days": null, "depends_on": [],
        "milestone": false, "status": "Done", "percent_complete": 100}
     ]
   }
   ```

   Dates are `YYYY-MM-DD` (or DD/MM/YYYY in CSV), `null` when unknown. `duration_days` is a whole number or `null`. `depends_on` lists task IDs (in CSV: separated by semicolons). `milestone` is true or false (in CSV: yes or no). `percent_complete` is 0 to 100 or `null`.
3. **Run the renderer.** The script is at `skills/gantt-chart/scripts/gantt.py` inside this plugin (in Claude Code: `${CLAUDE_PLUGIN_ROOT}/skills/gantt-chart/scripts/gantt.py`). It needs Python 3; the Excel and PowerPoint outputs also need `openpyxl` and `python-pptx`.

   ```
   python3 "<script path>" --input "<tasks file>" --out-dir "<folder>" --name "<plan name>" \
     --day-mode calendar --formats html,xlsx,pptx
   ```

   - Use `--day-mode working` if the user chose working days (Monday to Friday; public holidays are not excluded).
   - If the script stops with a date format error, ask the user which format the dates use, then run again with `--date-format dmy` or `--date-format mdy`. If the summary has a `date_note`, mention it.
   - If `openpyxl` or `python-pptx` is missing, run with `--formats html`, tell the user, and give them `pip install openpyxl python-pptx`. Do not install packages without asking.
   - If you cannot run code (for example in Claude chat without code execution), do not pretend you ran it. Show the normalised task table, the unscheduled list and the checks instead, and say the chart files need code execution.
4. **Read the JSON summary** the script prints: counts, `critical_path`, `unscheduled_ids`, `invalid_ids` and `warnings`.
5. **Report** using the output format below.

## What the script checks

- **Unscheduled, needs dates:** tasks it cannot place, with the reason (for example "Has a duration but no start date or dependency").
- **Circular dependencies:** tasks that depend on each other in a loop. Tasks in the loop that need their dependencies for a start date stay unscheduled.
- **Unknown dependencies:** IDs in `depends_on` that are not in the plan.
- **End before start:** shown in the checks and not drawn.
- **Missing owners**, duplicate IDs, dates or durations it cannot read, durations that do not match the dates, and tasks that start before a dependency finishes.

## What gets produced

```
<folder>/<plan-slug>-gantt.html   interactive chart: task table and bars, day/week/month zoom (and Ctrl + scroll),
                                   milestones as diamonds, dependency arrows, critical path toggle, phase groups,
                                   hover details, today line, unscheduled list and checks; works offline and prints
<folder>/<plan-slug>-gantt.xlsx   Gantt sheet with bars drawn by conditional formatting (edit Start or End and
                                   they move), Days formula, critical and milestone colours, today column;
                                   Tasks sheet (all data) and Checks sheet (every issue)
<folder>/<plan-slug>-gantt.pptx   16:9 deck: title slide, Gantt slides (about 18 tasks each) and a Gaps and checks slide
```

## Output format

```
## Gantt chart ready: <plan name>
<start date> to <end date>, durations in <calendar | working> days.

**Files**
- HTML: <path>
- Excel: <path>
- PowerPoint: <path>

**On the chart:** <n> of <total> tasks, <n> milestones.
**Critical path:** <ID > ID > ID ...> (<n> tasks with zero float).

**Unscheduled, needs dates (<n>)**
| ID | Task | What is missing |
|---|---|---|
| ... | ... | ... |
(or "None. Every task has dates or can be derived.")

**Checks (<n>)**
- <each warning in plain words: circular or unknown dependency, end before start, missing owner, ...>
(or "No issues found.")

**Assumptions:** <calendar or working days, date format used, anything else you assumed>
```

## Before handing over

End with one line: "Nothing was sent or uploaded. Check the dates, owners and dependencies with the people doing the work, fill the gaps above, then run the chart again."
