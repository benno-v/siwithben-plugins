---
name: weekly-priorities
description: Pull the top 3 priorities for the week from the latest status report and meeting notes, with why each matters, its source, and what to chase up. Use when the user asks "what should I focus on this week", wants their weekly priorities, or asks what to chase after a status report or meeting.
---

# Weekly priorities

Turn the latest status report and meeting notes into a short, ranked list of what actually matters this week — not a restated task list.

## Ground rules

- Work only from what the user gives you or what you can read in the connected folder. Never invent figures, dates, names or owners. Where something is missing, write "Not provided" or "TBC".
- Every priority must carry a source file or quoted source (e.g. "status-report-week8.md" or "notes the user pasted").
- If key inputs are missing (no recent status report or notes to work from), ask for them once, in one short numbered list, then continue with what you have.
- Exactly 3 priorities — if there are more good candidates, pick the 3 with the highest impact on schedule, budget or risk and mention the rest briefly under "also worth a look".
- Plain business English, short bullets, no jargon.

## Inputs to look for

The latest status report and/or meeting notes. Before asking the user for anything, check the connected folder / current working directory for status reports, meeting notes or similar project files and read the most recent ones by date — only ask if nothing suitable is found there and nothing was pasted. Open items, blockers, overdue actions, upcoming milestones, and anything flagged as a risk or decision.

Note: the weekly status report itself is produced by a separate skill, `/pm-status-report:status-report` — this skill reads from status reports and notes, it does not write them.

## Method

1. Find the most recent status report and/or meeting notes. If more than one candidate exists and it's not obvious which is latest, ask once.
2. List candidate items: blockers, overdue actions, items due this week, open decisions, and anything marked Amber/Red or high-risk.
3. Rank by what would most hurt the project this week if ignored: things blocking other work, approaching deadlines, and anything a stakeholder is waiting on usually rank above routine tasks.
4. Pick the top 3. For each, say why it matters in one sentence tied to schedule, budget, risk or a stakeholder commitment — not just "it's on the list".
5. Separately, list what to chase: open questions, overdue responses from others, or decisions still pending from someone else.

## Output format

```
# Weekly priorities: <Project name or "Not provided">
Week of: <date or TBC> · Based on: <source file(s) or "notes provided">

## Top 3 this week
1. **<priority>** — <why it matters, one sentence> — Source: <file/quote>
2. **<priority>** — <why it matters, one sentence> — Source: <file/quote>
3. **<priority>** — <why it matters, one sentence> — Source: <file/quote>

## Also worth a look
- <item> — Source: <file/quote>

## What to chase
- <open question or overdue item> — from: <who, if given> — Source: <file/quote>
```

## Before handing over

Add one line: "These priorities are ranked from what's in your notes — sanity-check them against anything that happened after they were written."
