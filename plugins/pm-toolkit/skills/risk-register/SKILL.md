---
name: risk-register
description: Build a project risk register with likelihood and impact ratings, a 3x3 risk matrix, mitigation actions and suggested owners. Use when the user asks for a risk register, risk log, risk assessment, RAID risks, or the top risks for a project.
---

# Risk register

## Ground rules

- Work only from what the user gives you. Never invent figures, dates, names, budgets or percentages. Where something is missing, write "Not provided" or "TBC".
- If key inputs are missing, ask for them once, in one short numbered list, then continue with what you have. Do not ask a second round of questions.
- Use the output format below exactly, every time, so documents look the same across projects.
- Plain business English, short bullets, no jargon.

## Inputs to look for

Project type, industry, size and timeline, key technology or suppliers, team situation, and any risks the user already knows about. Ask how many risks they want if unclear; default to 10.

## Method

1. Cover a spread of categories: technical, schedule, cost, people/resources, stakeholders/organisational, external (suppliers, regulation, market) and project-management risks.
2. Write each risk as cause → event → effect: "Because <cause>, <event> may happen, leading to <effect>."
3. Rate Likelihood (L) and Impact (I) as High (3), Medium (2) or Low (1). Score = L × I. Rating: 6–9 High, 3–4 Medium, 1–2 Low.
4. Ratings are your judgement from the context given; state that they are draft. Suggest owners by role (e.g. "Technical lead"), never by invented personal names.
5. Mitigation should be a concrete action; add a contingency for every High risk.
6. Sort the register by score, highest first.

## Output format

```
# Risk register: <Project>
Draft ratings for team review · Date: <date or TBC>

| ID | Category | Risk (cause → event → effect) | L | I | Score | Rating | Mitigation | Contingency | Suggested owner |
|---|---|---|---|---|---|---|---|---|---|
| R1 | ... | ... | H | H | 9 | High | ... | ... | ... |

## Risk matrix
|              | Low impact | Medium impact | High impact |
|---|---|---|---|
| **High likelihood**   | R.. | R.. | R.. |
| **Medium likelihood** | R.. | R.. | R.. |
| **Low likelihood**    | R.. | R.. | R.. |

## Top 3 to act on now
1. ...
```

The table is formatted so it can be pasted straight into Excel or Google Sheets.

## Before handing over

Add one line: "Review ratings and owners with your team and confirm each owner has agreed before you publish this register."
