---
name: morning-brief
description: A short, read-only morning brief from TASKS.md (and today's calendar if connected) with what is overdue, due today and this week, what is waiting on others, proposed tasks that need approval, today's meetings with their related open tasks, and three suggested focus items with a reason. Never sends anything or changes the tracker. Use when the user asks for a morning brief, daily brief, what's on today, what's due, what's overdue, what to focus on, or when a scheduled morning task runs.
---

# Morning brief

Give the user a two-minute read of their day from `TASKS.md`, the single task tracker. Read only.

## Ground rules

- **Read only.** Do not change `TASKS.md`, run a sweep, or edit, send or reply to anything in any app.
- **Never sends.** The brief appears in the session. Only if the user explicitly asks, create a **draft** email to the user's own address and nobody else; never send it.
- Use only what is in `TASKS.md` and the calendar. Do not invent owners, dates or meetings.
- Short. Plain British English, no em dashes.

## Inputs

1. `TASKS.md` in the working folder (Cowork: the selected folder; Claude Code: the current directory). If you can run code, use `python3 <plugin>/scripts/tasks_md.py show --tasks TASKS.md` (in Claude Code: `${CLAUDE_PLUGIN_ROOT}/scripts/tasks_md.py`); otherwise read the file. If there is no `TASKS.md`, say so and suggest the `sweep` skill. Stop.
2. Today's date (and the user's time zone).
3. Today's calendar events, only if Google Calendar (or another calendar) is connected. Otherwise write "Calendar not connected".

## Method

- **Overdue:** Open-section rows with a due date before today. Oldest first, with days overdue.
- **Due today** and **due this week** (to Sunday): Open-section rows.
- **Waiting on others:** status Waiting, or an owner who is not the user, due this week or overdue.
- **Needs your approval:** the count of "Proposed, needs approval" rows and the top 5 (oldest raised first) with the reason from Notes.
- **Meetings today:** each event with the open tasks that relate to it (same people, project or topic). Say "possible match" if you are not sure.
- **Top 3 focus:** pick from overdue, due today and blockers, with a one-line reason each (deadline, others waiting on it, meeting today).
- Flag unassigned open tasks and anything Blocked in one line.
- If "Last sweep" is more than 2 days old, add: "The tracker was last swept on <date>; ask me to sweep for anything newer."

## Output format

```
## Morning brief, <weekday> <d> <month>
**Focus today**
1. <T-ID action> (<owner>): <reason>
2. ...
3. ...

**Overdue (<n>):** T-001 Send revised policy wording (Priya Nair, 3 days)
**Due today (<n>):** ...
**Due this week (<n>):** ...
**Waiting on others (<n>):** ...
**Needs your approval (<n>):** top 5 with reason. Approve them in the dashboard or tell me.
**Meetings today:** 10:00 Weekly check-in: related T-002, T-009
**Watch:** <unassigned or blocked tasks, stale sweep>
```

Leave out an empty section rather than writing "none", except Overdue and Focus. Keep it under about 200 words.

## Before handing over

End with: "Owners and dates come from TASKS.md; check the source before you quote them in a report."
