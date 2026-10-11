---
name: sweep
description: Sweep connected sources (Gmail, Google Calendar, Slack, Notion, ClickUp, meeting notes in the folder, Apple Notes where a local connector exists) for committed actions since the last sweep and add them to TASKS.md, the single task tracker. Separates real commitments from passing remarks, de-duplicates across sources and against existing tasks, proposes anything uncertain for approval, and never changes an existing owner or due date silently. Use when the user asks to sweep, refresh or update the task tracker, pull actions or to-dos from email, Slack, calendar, meetings or a PM tool, find what they or others committed to, or when a scheduled task runs a sweep.
---

# Sweep

Pull every committed action from the user's connected sources into `TASKS.md`, without rebuilding the list. The tracker keeps one row per action with: ID, Action, Owner, Source, Raised, Due, Status, Notes.

## Ground rules

- **Read only in every source.** Never send, reply, react, comment, archive, label, move or change anything in Gmail, Slack, Calendar, Notion, ClickUp or any other app. Never message anyone.
- **`TASKS.md` is the single source of truth.** Write to it only through the scripts below, never by retyping the file.
- **Never delete a row.** Never change an existing row's owner or due date silently: list it under "Suggested updates" for the user to approve.
- **Mark a task done only on clear evidence** (a "sent" email with the thing attached, the PM tool status set to done, "booked" with a confirmation) and list it under "Probably done" for confirmation first.
- **Never invent owners or dates.** No owner in the source means a blank owner (shown as Unassigned). A vague date ("soon", "before UAT") stays blank and goes in Notes.
- Plain British English, short sentences, no em dashes.

## Modes

- **Interactive** (default, the user is in the session): show the summary, wait for approval, then write.
- **Scheduled** (the prompt says scheduled or Proposed-only, or no one is there to approve): add new rows **only** to "Proposed, needs approval" and update "Last sweep". Never touch existing rows, never mark anything done, never delete. Put merges, suggested updates and probably-done items in the report only.

## Files and scripts

`TASKS.md` lives in the user's working folder (Cowork: the selected folder; Claude Code: the current directory). The scripts are in `scripts/` inside this plugin (in Claude Code: `${CLAUDE_PLUGIN_ROOT}/scripts/`). They need only Python 3.

- `tasks_md.py init --tasks TASKS.md` creates an empty tracker (never overwrites). In interactive mode, ask before creating it. In scheduled mode, create it.
- `tasks_md.py show --tasks TASKS.md` prints every row, the revision, `last_sweep` and `next_id` as JSON. Run it first.
- `apply_changes.py --tasks TASKS.md --changes - [--dry-run] [--proposed-only]` applies the changes block (from stdin). It checks the revision, validates every op, keeps the last 5 versions in `.task-tracker-backups/`, writes atomically and logs every change in the "Change log" section. It writes nothing if `TASKS.md` has duplicate IDs (fix them with `tasks_md.py validate` first) or changed while it was running (run it again).

If you cannot run code, do not pretend you did: show the summary and the rows to add as a markdown table for the user to paste in.

## Step 1: window and sources

1. Run `show`. The window is from `last_sweep` to now. First run (`never`): the last 7 days. Say which window you used.
2. Read each connected source for that window, read only:
   - **Gmail:** sent and received threads. The user's own sent mail is where most of their "I'll" commitments are.
   - **Google Calendar:** events in the window and the next 7 days; descriptions and attached notes. Events themselves are not tasks.
   - **Slack:** channels and DMs the user is in.
   - **Notion / ClickUp (or another PM tool):** tasks created, assigned or changed in the window, with assignee, due date and status.
   - **Meeting notes:** files in the folder (for example `meeting-notes/`, `inputs/`, `*.md`, `*.txt`, transcripts) changed in the window.
   - **Apple Notes:** only if a local connector for it is available.
3. List any source that is not connected or failed under "Not checked". Never guess what it contains.

## Step 2: extract committed actions only

A **committed action** is an explicit commitment by a named person:

- "I'll send ...", "I will ...", "Leave it with me" with a clear thing to do
- "X to do Y", "Action: X ...", "agreed X will ..."
- a task assigned to someone in a PM tool
- a direct request the person accepted ("Can you ...?" "Yes, I'll ...")

**Not** a committed action (list under "Not tracked", do not add):

- passing remarks, ideas and wishes: "we should ...", "it would be nice ...", "might be worth ...", "at some point"
- questions nobody accepted, FYI and newsletters, calendar events on their own

For each action capture: Action (verb first, one line), Owner (as written in the source), Source, Raised (date of the source), Due (only from the source; resolve "by Wednesday" from the source's own date, not today), Notes.

**Source format:** `<tool>: <item> (<YYYY-MM-DD>)` plus the link if there is one, for example `Gmail: "Purchase order" from Mei Chen (2026-10-09) https://...` or `ClickUp: CP-121 (2026-10-07) https://...`. Several sources are joined with `; `.

## Step 3: decide Open or Proposed

- **Open** (interactive mode only, after the user approves the summary): an explicit assignment in a PM tool; the user's own "I'll"; or an explicit commitment with **one clear owner** in the source's own words.
- **Proposed, needs approval**, with the reason in Notes:
  - anything inferred: an implied ask, an intention that may or may not be a commitment
  - unclear owner, including **two names in one paragraph** ("Sam and Jordan, one of you ...")
  - a due date you had to interpret
- In scheduled mode, everything new is Proposed.

## Step 4: de-duplicate

- Against `TASKS.md` and within this sweep. The same action with the same owner, or the same source thread, is one task.
- Merge into one row and join the sources in the Source column (a source-only update on an existing row is allowed; say so in the summary).
- If a duplicate carries a different owner or due date, do not change the row: add it to "Suggested updates".
- `apply_changes.py` also skips an `add` whose action and owner match an existing row, including Done rows, and one whose action matches a task rejected before (from the change log). A blank owner, `TBC`, `?` and `Unassigned` count as the same owner. If a done task genuinely recurs, make the action say which one (for example "Send the October report").

## Step 5: summary, then approval

Show this, short, before writing anything:

```
## Sweep: <window start> to <now>
Sources checked: <list>. Not checked: <list or "none">.

**New, committed (<n>)**
| Action | Owner | Due | Source |

**New, needs your approval (<n>)**
| Action | Owner? | Due? | Why it needs you | Source |

**Merged into existing tasks (<n>):** T-003 (added Gmail 2026-10-06 to Source) ...
**Suggested updates (<n>):** T-005 due 2026-10-23 to 2026-10-21 (ClickUp CP-118, 2026-10-09) ...
**Probably done (<n>):** T-001, evidence: <quote>, <source> ...
**Not tracked (<n>):** "<quote>" (<source>) ...

Approve all, or tell me what to change. Nothing is written until you say so.
```

In scheduled mode, skip the wait: write the Proposed rows (step 6) and end with the same summary, headed "Scheduled sweep: added to Proposed only".

## Step 6: write

Build one changes block and pipe it to `apply_changes.py`, first with `--dry-run`, then for real:

```json
{"base_revision": "<revision from show>", "generated": "<ISO time>", "source": "sweep",
 "last_sweep": "<YYYY-MM-DD HH:MM now>",
 "ops": [
  {"op": "add", "fields": {"action": "...", "owner": "...", "source": "...", "raised": "YYYY-MM-DD", "due": "", "status": "Open", "notes": ""}},
  {"op": "add", "fields": {"action": "...", "owner": "", "source": "...", "raised": "...", "status": "Proposed", "notes": "Owner unclear: ..."}},
  {"op": "update", "id": "T-003", "fields": {"source": "<old source>; <new source>"}},
  {"op": "update", "id": "T-005", "fields": {"due": "2026-10-21"}},
  {"op": "complete", "id": "T-001", "date": "2026-10-09"}
 ]}
```

- Include `update` (owner, due, status) and `complete` ops only for items the user approved.
- Scheduled mode: add `--proposed-only`; the script then only adds Proposed rows and sets Last sweep.
- The revision covers only the task rows, so a new Last sweep line or change log entry never causes a refusal. If rows changed meanwhile (someone edited `TASKS.md`), a block with only `add` ops still goes ahead (the duplicate check guards it), but a block with `update` or `complete` ops is refused as a whole: run `show` again and rebuild it. Never use `--force` in a sweep.
- Read `skipped` in the result: duplicates of existing, done or rejected tasks are reported there, not added.
- Report the new IDs, anything skipped with the reason, and the new revision.

## Validation checkpoint (before anything goes into a status report)

Claude can read an intention as a commitment, and can attach the wrong owner when two names share a paragraph. So:

1. Every owner and due date in a new row must be checkable against the quoted source. That is what the Source column is for.
2. Before rows from this tracker go into a status report or an email, open the source for each new or changed row and check the owner and due date.
3. When in doubt, it stays in "Proposed, needs approval" with the reason.

End every sweep with: "Check the owner and due date of each new row against its source before it goes into a report."
