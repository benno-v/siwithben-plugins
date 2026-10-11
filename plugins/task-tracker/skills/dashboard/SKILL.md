---
name: dashboard
description: Render the task tracker (TASKS.md) as a visual dashboard with KPI cards, overdue, due this week, open by owner and done panels, tick boxes and inline edits, and a "Proposed, needs your approval" panel with Approve, Reject and Edit; then apply the changes the user pastes back (a task-tracker-changes block or tasks-changes.json) with a revision check. Optional mirror to a Notion database on request. Use when the user asks for the task dashboard, a visual or tick-box view of their tasks, to publish it as an artifact, pastes a task-tracker-changes block, mentions tasks-changes.json, or asks to apply dashboard changes or sync tasks to Notion.
---

# Dashboard

Show `TASKS.md` as a dashboard the user can tick and edit, then bring their changes back into `TASKS.md` safely.

## Why changes come back by paste

`TASKS.md` in the user's folder is the single source of truth. The dashboard cannot write it: a local HTML file has no access to the folder, and a Claude artifact can only keep text in its own storage, not in browser local storage or local files ([What are artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them), [Artifacts in Cowork](https://support.claude.com/en/articles/14729249-use-artifacts-in-claude-cowork)). So the page collects ticks and edits as a list of changes. **Copy changes** gives a block to paste into the session; **Download changes** saves `tasks-changes.json` for the folder. This is the export pattern the [Claude Code artifacts docs](https://code.claude.com/docs/en/artifacts.md) recommend.

## Ground rules

- Never change `TASKS.md` except through `apply_changes.py`, and only after the user confirms the dry run.
- Never use `--force` without showing the user the "changed since" list and getting a clear yes. Dashboard blocks never need it: `--force` only matters for ops without a `before` snapshot (hand-written blocks), and it never overrides a snapshot check.
- Delete nothing except the applied `tasks-changes.json` (rename it, see below). Never delete Notion pages.
- Proposed tasks have no tick box on purpose: they need the user's input (approve, edit or reject), not a tick.
- Plain British English, no em dashes.

## Scripts

In `scripts/` inside this plugin (in Claude Code: `${CLAUDE_PLUGIN_ROOT}/scripts/`). Python 3 only.

- `render_dashboard.py --tasks TASKS.md --out dashboard.html` writes a self-contained page (no external files) with the revision of `TASKS.md` embedded.
- `apply_changes.py --tasks TASKS.md --changes <file or -> [--dry-run] [--force]` accepts the fenced block (with any text around it) or raw JSON.

If you cannot run code, say so; do not pretend you rendered or applied anything.

## Render and open

1. Find `TASKS.md` in the working folder. If there is none, suggest the `sweep` skill and stop.
2. Run `render_dashboard.py`; it writes `dashboard.html` next to `TASKS.md` and prints counts and any validation errors and warnings. Mention errors in one line, plus any warning about rows that are not parsed (a row after a blank line, without a leading `|`, or under a heading such as `## Open tasks`): those tasks are not on the dashboard. Tasks with a duplicate ID are shown without controls until the ID is fixed.
3. Show it:
   - **Cowork:** offer to publish the page as an artifact. Artifacts created on or after 19 August 2026 can keep unapplied ticks in their own storage between opens. Older Cowork live artifacts are view only now, so render a fresh one. Or open `dashboard.html` from the folder in a browser.
   - **Claude Code:** give the path to open in a browser, or publish it as an artifact if artifacts are available in the session.
4. Tell the user in two lines: tick what's done, use Edit for owner, due date, status or wording, Approve or Reject proposed tasks; then click **Copy changes** and paste the block here (or **Download changes** into this folder).

## Apply changes

Triggered by a pasted ` ```task-tracker-changes ` block, or a `tasks-changes.json` in the folder when the user asks to apply dashboard changes.

1. Dry run: pass the pasted text on stdin (`--changes -`) or the file path, with `--dry-run`.
2. Show the result in plain words:

   ```
   Ready to apply to TASKS.md (revision e91924acdb08):
   - Mark done: T-003 Send updated Q4 budget forecast to finance
   - Edit T-002: owner Sam Taylor to Priya Nair; due 14 Oct to 20 Oct
   - Approve: T-007 Organise a team lunch after go-live (no owner yet)
   - Add: T-009 Order launch cake (Sam Taylor)
   Skipped: <op and reason, or "none">
   Apply these?
   ```

3. On yes, run without `--dry-run`. Report the new revision and the `backup` path (the last 5 versions are kept in `.task-tracker-backups/`).
4. If the task rows changed since the dashboard was rendered (a sweep added a row, someone edited the file), the script checks each op against its `before` snapshot. Ops on unchanged rows are applied; the rest are listed under `skipped` with the reason. For an edit, only the fields changed since are skipped (the entry has a `field`), the rest of the edit is applied. Show the skipped items and `changed_since`, and offer to re-render so the user can redo them. A new Last sweep line or change log entry alone changes nothing.
5. If the script **refuses** (exit 2 or 1):
   - "already applied": say so and stop.
   - "no before snapshot" (a hand-written block): show `changed_since` and offer to rebuild the block, or `--force` after the user has checked the rows.
   - "duplicate IDs": nothing was written; run `tasks_md.py validate`, fix the IDs with the user, then apply again.
   - "changed while these changes were being applied": run the same command again.
6. After applying a `tasks-changes.json`, rename it to `tasks-changes.applied-<YYYYMMDD-HHMM>.json` so it is not applied twice. Delete nothing else.
7. Re-render the dashboard so it shows the new revision. Unapplied changes kept in artifact storage survive the re-render, except for tasks that changed in `TASKS.md` meanwhile; the page says which ones it dropped.

Approving a task with no owner is allowed; say "approved without an owner" and suggest one.

## Changes block format

````
```task-tracker-changes
{"base_revision":"<12 hex>","generated":"<ISO time>","ops":[
 {"op":"complete","id":"T-004"},
 {"op":"update","id":"T-002","fields":{"due":"2026-10-20","owner":"Sam"}},
 {"op":"approve","id":"T-009"},
 {"op":"reject","id":"T-010"},
 {"op":"add","fields":{"action":"...","owner":"...","due":"YYYY-MM-DD"}}]}
```
````

Ops from the dashboard also carry a `before` snapshot of the row. `complete`, `approve` and `reject` are skipped if the row no longer matches it; `update` skips only the fields that changed since. Edit sends only the fields the user changed: a due date that is not a real date (`TBC`, `Fri`) and a status outside the list are kept unless the user picks a new one. The revision is a fingerprint of the Open, Proposed and Done rows only. `complete` moves a row to Done with "done <date>" in Notes; `approve` moves a proposed row to Open; `reject` removes a proposed row and records it in the change log; every applied op is logged as `YYYY-MM-DD HH:MM dashboard: <op> T-xxx`.

## Optional: mirror to Notion (on request only)

Only when the user asks and the Notion connector is connected.

- Use a database with the properties from my [Notion Action List kit](https://github.com/benno-v/siwithben-plugins/tree/main/kits/notion-action-list): `Task` (title), `Owner`, `Due` (date), `Status` (select), `Priority`, `Source`, `Source link` (URL), `Notes`. Recommend adding a `Tracker ID` text property so rows match exactly; without it, match on Task plus Owner.
- Mirror Open and Done rows only, not proposed ones. Status: Open to Not started, In progress to In progress, Waiting and Blocked to Blocked, Done to Done. Put the first link from Source in `Source link`.
- Show the plan first (create n, update n, unchanged n) and wait for a yes. Create and update pages only; **never delete or archive a Notion page**, even if the task left `TASKS.md`.
- `TASKS.md` stays the source of truth. Edits made in Notion are not read back; tell the user to make changes in the dashboard or `TASKS.md`.

## Before handing over

End with: "Ticks and edits only reach TASKS.md when you paste the changes back. Check owners and due dates against the Source column before they go into a report."
