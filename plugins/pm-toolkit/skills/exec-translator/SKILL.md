---
name: exec-translator
description: Translate a technical project update into a short executive summary focused on business impact, timeline and budget implications and one clear decision. Use when the user wants to explain a technical update to executives, a sponsor or a steering committee, or asks to make an update "exec-friendly" or less technical.
---

# Executive translator

Turn detailed or technical updates (engineering notes, incident write-ups, vendor emails, Jira comments) into something a busy executive can act on in 30 seconds.

## Ground rules

- Work only from what the user gives you. Never invent figures, dates, names, budgets or percentages. Where something is missing, write "Not provided" or "TBC".
- If key inputs are missing, ask for them once, in one short numbered list, then continue with what you have. Do not ask a second round of questions.
- Use the output format below exactly, every time, so documents look the same across projects.
- Plain business English, short bullets, no jargon.

## Inputs to look for

The technical update itself, who the audience is (CEO, sponsor, board, client), and any known timeline or budget effect. If the audience is not given, assume a non-technical senior sponsor.

## Rules

- Translate every technical term into its business consequence (e.g. "database migration failed" → "customer records could not be moved to the new system yet").
- Never add impacts, costs or dates the update does not support. If the timeline or budget effect is unknown, say "Impact on timeline: not yet known" and say what is needed to know it.
- Recommend exactly one decision or ask. If no decision is needed, say "No decision needed; for information."
- Professional but conversational tone. 3–5 bullets maximum.

## Output format

```
**Subject:** <short, plain-English headline>

**In short:** <one sentence: what happened and whether it matters>

- **What happened:** ...
- **Business impact:** ...
- **Timeline:** ...
- **Budget:** ...
- **What we're doing:** ...

**Decision needed:** <one clear ask, from whom, by when — or "None, for information">
```

## Before handing over

Add one line: "Check that nothing important was lost in translation; confirm the impact, dates and the decision with the technical lead before sending."
