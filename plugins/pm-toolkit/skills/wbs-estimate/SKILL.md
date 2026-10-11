---
name: wbs-estimate
description: Break a project or requirement into a work breakdown structure (WBS) with three-point PERT estimates, dependencies, skills and risks per task. Use when the user asks for a WBS, task breakdown, effort or time estimate, PERT estimate, or how long a feature or project will take.
---

# WBS with PERT estimates

## Ground rules

- Work only from what the user gives you. Never invent figures, dates, names, budgets or percentages. Where something is missing, write "Not provided" or "TBC".
- If key inputs are missing, ask for them once, in one short numbered list, then continue with what you have. Do not ask a second round of questions.
- Use the output format below exactly, every time, so documents look the same across projects.
- Plain business English, short bullets, no jargon.

## Inputs to look for

The requirement or deliverable, the team or skills available, any fixed deadline, and how detailed the breakdown should be. If the user gives no team size, estimate effort in hours only and do not convert to calendar dates.

## Method

1. Break the work into 3–7 phases or deliverables, then into tasks small enough to estimate (roughly 2–40 hours each). Include the work people usually forget: requirements clarification, reviews, testing, fixes, documentation, deployment and handover.
2. For each task give three estimates in hours: Optimistic (O), Most likely (M), Pessimistic (P).
3. Calculate the PERT expected time E = (O + 4M + P) / 6 and the standard deviation SD = (P − O) / 6. Round to one decimal place.
4. These hour estimates are your professional judgement, so label them clearly as estimates for the team to validate. Never present them as facts from the user.
5. Total E for the whole project. Project SD = square root of the sum of the task variances (SD²). Give a ~95% range as Total E ± 2 × project SD.

## Output format

```
# WBS and estimate: <Project or requirement>
Estimates are draft assumptions for team review (hours).

| WBS | Task | O | M | P | E (PERT) | Depends on | Skills | Risk / note |
|---|---|---|---|---|---|---|---|---|
| 1 | <Phase> | | | | <sum> | | | |
| 1.1 | <Task> | 2 | 4 | 8 | 4.3 | – | ... | ... |

## Summary
- Total expected effort (E): <x> hours
- Project standard deviation: <x> hours
- ~95% range: <low> – <high> hours
- Biggest uncertainty drivers: <top 3 tasks with the widest O–P spread>

## Assumptions
- ...
```

## Before handing over

Add one line: "These are starting estimates. Walk through them with the people doing the work and adjust using your own historical data before committing to dates."
