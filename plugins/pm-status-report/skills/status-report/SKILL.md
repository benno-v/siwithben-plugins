---
name: status-report
description: Write a weekly project status report in a fixed, executive-friendly format with an overall RAG (Red/Amber/Green) rating. Use when the user asks for a status report, weekly update, project update, or sponsor/steering summary, or pastes rough notes about progress, blockers and milestones.
---

# Weekly project status report

You turn whatever the user gives you (bullet notes, a meeting summary, a task export, a Slack thread) into the same one-page report every time. Consistency is the point: a sponsor should be able to read any week's report in the same order.

## 1. Gather the inputs

Look for these in what the user provided. If something important is missing, ask once, in a single short list, then continue with what you have and mark gaps as "Not provided".

- Project name and reporting period (week ending date)
- Done this period
- In progress
- Blockers and issues
- Upcoming milestones with dates
- Budget position (e.g. % spent vs % complete) if known
- Schedule position (on track / at risk / delayed) if known
- Decisions or help needed from the reader

Never invent figures, dates, owners or percentages. If the user did not give a number, do not make one up.

## 2. Decide the RAG rating

Pick one overall status and give a one-sentence reason.

- **Green**: on track for scope, time and budget; no blocker needs escalation.
- **Amber**: at least one milestone or the budget is at risk, but there is a recovery plan the team can run itself.
- **Red**: a milestone will be missed or the budget exceeded without a decision or help from the reader.

If the user stated a status, keep it, but say so briefly if the evidence points elsewhere.

## 3. Write the report

Use exactly this structure and these headings. Keep it to one page. Plain business language, no technical jargon, short bullets.

```
# <Project name> — Status report, week ending <date>

**Overall status:** <🟢 Green | 🟠 Amber | 🔴 Red> — <one-sentence reason>

## Summary
<2–3 sentences a busy executive can read in 15 seconds.>

## Done this week
- ...

## In progress
- <item> — <owner if known> — <expected completion if known>

## Blockers and risks
- <issue> — <impact> — <what is being done / who owns it>

## Upcoming milestones
| Milestone | Due | Confidence |
|---|---|---|

## Budget and schedule
- Budget: ...
- Schedule: ...

## Decisions or help needed
- <a clear ask, with who and by when> (or "None this week")

## Next steps
- ...
```

## 4. Check before handing over

End with a short line, outside the report, reminding the user to check owners, dates and figures against the source before it goes to a sponsor. The report makes them consistent, not automatically correct.
