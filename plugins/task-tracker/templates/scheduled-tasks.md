# Scheduled tasks for the task tracker

Where this goes: a scheduled task in Claude Cowork, in the Claude desktop app. Create one scheduled task per block below, give it access to the folder that holds your `TASKS.md`, and paste the prompt.

Scheduled tasks only run while the Claude desktop app is open. See [Use Claude Cowork on web, desktop and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile). If a run doesn't happen, nothing is lost: each sweep reads everything since the "Last sweep" line, however long ago that was.

All three only read your apps. None of them sends a message, and only the sweep writes to `TASKS.md`, and then only into "Proposed, needs approval".

---

## 1. Morning brief

Schedule: weekdays at 07:00

```
Run the task-tracker morning-brief skill on TASKS.md in this folder, with today's calendar if it is connected.
Read only: do not change TASKS.md and do not send, draft or reply to anything.
Keep it under 200 words and end with the three things I should focus on today and why.
```

---

## 2. Sweep, Proposed only

Schedule: weekdays at 08:00, 12:30 and 16:30 (three scheduled tasks with the same prompt, or one with three times if your version allows it)

```
Run the task-tracker sweep skill in scheduled mode on TASKS.md in this folder.
Sources: Gmail, Google Calendar, Slack, Notion, ClickUp and the meeting notes in this folder, since "Last sweep".
Proposed-only mode: add new actions only to "Proposed, needs approval" (apply_changes.py --proposed-only)
and update Last sweep. Do not change, complete or delete existing rows. Do not message anyone.
End with the summary: new proposed tasks, merges, suggested updates, probably done, not tracked, sources not checked.
```

---

## 3. Friday review

Schedule: Fridays at 15:00

```
Weekly task review for TASKS.md in this folder, read only.
1. Run the task-tracker sweep skill in scheduled mode first (Proposed only), so the list is current.
2. Then give me: done this week; still open with owner and due date; overdue; waiting on others;
   everything in "Proposed, needs approval" with the reason; open tasks with no owner or no due date;
   and next week's deadlines.
3. List every owner and due date that changed this week (from the Change log) with its source,
   so I can check them before anything goes into my status report.
Then render the dashboard with the task-tracker dashboard skill so I can approve and tick in one go.
Do not send anything.
```
