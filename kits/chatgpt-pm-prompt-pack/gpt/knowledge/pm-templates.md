# PM Templates by SI with Ben

Knowledge file for the "PM Prompt Pack by SI with Ben" GPT. Written by Benjamin Vermeulen (SI with Ben, @SIwithBen).

These are the five templates I use for everyday project management drafting. Each section has three parts:

- **Inputs to collect**: what to look for in the user's message. Key inputs are the ones worth asking about if missing. Everything else can be marked "Not provided" or "TBC".
- **Method**: how to build the artefact.
- **Output skeleton**: the exact format to return. Keep headings, order and table columns exactly as shown. Text in [square brackets] is replaced with content.

General rules for all five templates:

- Never invent figures, dates, names or budgets. Use "Not provided" for missing input and "TBC" for decisions the project still has to make.
- Owners are roles, not people.
- Tables are simple Markdown tables, one value per cell, no line breaks inside cells, so they paste cleanly into Excel.
- Every artefact ends with the review reminder and a short next steps offer (see the GPT instructions).

---

## Template 1: Project Charter

### Inputs to collect

Key inputs:

1. Project name
2. Context in 2 to 3 sentences: what the project is and why now
3. Sponsor or approving body (role)
4. Target timeframe or deadline
5. Budget, if known

Useful extras: known constraints (regulatory, technical, resourcing), stakeholders, what is explicitly out of scope, existing systems involved.

### Method

1. State the purpose as the business problem or opportunity, not the solution.
2. Write 3 to 5 objectives in SMART format: Specific, Measurable, Achievable, Relevant, Time-bound. Every objective needs a measure and a date. If the user gave no target value or date, write the objective with "[target TBC]" or "[date TBC]" rather than making one up.
3. Define scope as in scope and out of scope. Out of scope is as important as in scope; include at least two items if the context suggests them, and label them as proposed.
4. Group stakeholders into primary (decide or are directly affected), secondary (contribute or are indirectly affected) and external (outside the organisation: regulators, suppliers, customers, partners).
5. List high-level requirements as capabilities or outcomes, not detailed specifications.
6. Separate constraints (fixed limits: budget, deadline, regulation, technology) from assumptions (things believed to be true that must be validated).
7. Success criteria describe how the sponsor will judge the project at closure. Link them to the objectives.
8. Key milestones are high level, typically 4 to 7. Use dates only if the user gave them or they follow directly from the given timeframe; otherwise use "TBC" or relative timing (for example "Month 1").
9. Keep the whole charter under 2 pages. Bullets throughout; no long paragraphs.

### Output skeleton

```
# Project Charter: [Project name]

**Sponsor:** [role or "Not provided"]
**Project manager:** [role or "Not provided"]
**Timeframe:** [timeframe or "Not provided"]
**Budget:** [amount or "Not provided"]
**Version:** Draft 0.1

## 1. Purpose
- [Business problem or opportunity]
- [Why now]

## 2. Objectives (SMART)
1. [Specific outcome] measured by [measure], achieving [target] by [date].
2. ...

## 3. Scope
**In scope**
- ...

**Out of scope**
- ...

## 4. Stakeholders
**Primary**
- [Role]: [interest or responsibility]

**Secondary**
- [Role]: [interest or responsibility]

**External**
- [Organisation or group]: [interest or responsibility]

## 5. High-level requirements
- ...

## 6. Constraints
- ...

## 7. Assumptions to validate
- [Assumption] (validate with: [role])

## 8. Success criteria
- ...

## 9. Key milestones
| Milestone | Target date | Owner (role) |
|---|---|---|
| [Milestone] | [date or TBC] | [role] |

## 10. Approval
- Sponsor sign-off: TBC
```

---

## Template 2: WBS and Three-Point (PERT) Estimation

### Inputs to collect

Key inputs:

1. The requirement or deliverable to break down (pasted text)
2. Team roles available (for example developer, designer, QA)
3. Level of detail wanted (high level or detailed), default detailed
4. Any fixed constraints (deadline, technology, team size)

Useful extras: definition of done, existing assets that can be reused, known risks.

### Method

1. Decompose the requirement into a work breakdown structure with numbered levels (1, 1.1, 1.1.1). Stop at work packages that one role can deliver and estimate, typically 4 to 40 hours each. Include project management, testing and deployment work, which are often forgotten.
2. For every lowest-level task give three estimates in hours:
   - O = optimistic (everything goes well)
   - M = most likely
   - P = pessimistic (realistic bad case, not catastrophe)
   - Rule: O <= M <= P.
3. Calculate for each task:
   - Expected effort E = (O + 4M + P) / 6
   - Standard deviation SD = (P - O) / 6
4. Totals:
   - Total E = sum of task E values
   - Total SD = square root of the sum of task SD squared (tasks treated as independent). Show this formula.
   - Confidence range = Total E plus or minus 2 x Total SD (approximately 95% if the estimates are reasonable).
5. Dependencies use task IDs (for example "1.2" or "None").
6. Required skills or resources are roles, not names.
7. Risks per task: one short phrase for the main estimating or delivery risk.
8. Add a by-role summary that sums E per role.
9. State clearly that these are planning estimates for the team to validate. Hours are effort, not elapsed calendar time.

### Output skeleton

```
# WBS and Estimates: [Project or requirement name]

**Basis:** [one line summarising the requirement]
**Units:** effort hours. Estimates are planning estimates for the team to validate.

## 1. Work breakdown structure
- 1 [Phase or deliverable]
  - 1.1 [Work package]
    - 1.1.1 [Task]
    - 1.1.2 [Task]
  - 1.2 [Work package]
- 2 [Phase or deliverable]
  - 2.1 ...

## 2. Task estimates
| ID | Task | Hours (O) | Hours (M) | Hours (P) | Hours (E) | SD | Depends on | Skills / role | Key risk |
|---|---|---|---|---|---|---|---|---|---|
| 1.1.1 | [Task] | [O] | [M] | [P] | [E] | [SD] | [IDs or None] | [role] | [risk] |

## 3. Summary
- Formula: E = (O + 4M + P) / 6; SD = (P - O) / 6
- Total expected effort (E): [sum] hours
- Total SD: square root of (sum of SD squared) = [value] hours
- Confidence range (E plus or minus 2 SD): [low] to [high] hours
- Number of tasks: [count]

## 4. Effort by role
| Role | Tasks | Hours (E) | Share of total |
|---|---|---|---|
| [Role] | [count] | [hours] | [percent] |
| Total | [count] | [hours] | 100% |

## 5. Assumptions and notes
- ...
```

---

## Template 3: Risk Identification and Register

### Inputs to collect

Key inputs:

1. Project type (for example website redesign, mobile app, marketing campaign)
2. Industry or sector
3. Project specifics: scope, timeframe, budget, team, key dependencies
4. Number of risks wanted, default 10

Useful extras: known issues, regulatory context, risk appetite of the sponsor.

### Method

1. Default to the top 10 risks. If the user asks for more than 15, warn once: "Asking for many risks at once tends to lower quality and produce generic items. I suggest the top 10 first, then a second pass on one category." Then do what the user asked.
2. Cover all four categories, with at least one risk each where relevant:
   - Technical (technology, integration, performance, security, quality)
   - External (regulatory, suppliers, market, customers, third parties)
   - Organisational (resources, priorities, funding, stakeholder support, skills)
   - Project management (estimates, scope, planning, communication, dependencies)
3. Write each description in cause, event, effect form: "Because of [cause], [event] may occur, leading to [effect]." Make them specific to the project, not generic.
4. Rate probability and impact as H, M or L. Convert H = 3, M = 2, L = 1. Score = probability x impact (1 to 9).
5. Rating bands: 6 to 9 = High, 3 to 4 = Medium, 1 to 2 = Low.
6. Mitigation is a concrete action that reduces probability or impact, starting with a verb. Add a contingency only if it fits in the same cell briefly.
7. Owner is a recommended role.
8. Sort the register by score, highest first.
9. After the table, list the top 3 risks to discuss with the sponsor in one line each.

### Output skeleton

```
# Risk Register: [Project name or type]

**Context:** [project type], [industry]. [one line of specifics]
**Scoring:** H = 3, M = 2, L = 1. Score = Probability x Impact (1 to 9). 6 to 9 High, 3 to 4 Medium, 1 to 2 Low.

| ID | Category | Risk description | Probability (H/M/L) | Impact (H/M/L) | Score (1-9) | Rating | Mitigation | Owner (role) |
|---|---|---|---|---|---|---|---|---|
| R01 | [Technical/External/Organisational/Project management] | [cause, event, effect] | [H/M/L] | [H/M/L] | [score] | [High/Medium/Low] | [action] | [role] |

## Top 3 to discuss with the sponsor
1. [ID]: [one line why]
2. ...
3. ...

## Notes
- Ratings are initial assessments for the team to review.
- [Any assumptions made]
```

---

## Template 4: Communication (Executive) Translator

### Inputs to collect

Key inputs:

1. The technical update (pasted text)
2. Audience (for example CEO, board, sponsor, client director), default senior sponsor
3. Any known cost or date figures not in the update

### Method

1. Identify what changed, why it matters to the business, and what it costs in time and money.
2. Write 3 to 5 bullets maximum. Each bullet is one or two sentences.
3. Focus on business impact: customers, revenue, operations, compliance, reputation. Remove jargon; if a technical term is unavoidable, explain it in a few words.
4. Include timeline and budget implications. Only use figures from the update or the user. If the implication is unknown, say so ("Budget impact: not yet quantified").
5. Decision needed: include exactly one decision, and only if the update genuinely requires one. Frame it as a clear choice with a deadline if given. If no decision is required, write "No decision needed".
6. Tone: professional but conversational, as if speaking to a busy executive. No blame.

### Output skeleton

```
# Executive Summary: [Topic]

**For:** [audience]
**Date:** [date or "Not provided"]

- **What happened:** [plain-language summary]
- **Business impact:** [effect on customers, revenue, operations or compliance]
- **Timeline:** [implication or "No change"]
- **Budget:** [implication or "Not yet quantified"]
- **[Optional fifth bullet: what we are doing about it]**

**Decision needed:** [one decision, options and deadline] OR No decision needed
```

---

## Template 5: Weekly Status Report

### Inputs to collect

Key inputs:

1. Reporting period (week ending date)
2. Tasks completed
3. Tasks in progress
4. Blockers
5. Upcoming milestones with dates
6. Budget status (for example percentage spent and whether that matches plan)
7. Schedule status: on track, at risk or delayed

Useful extras: project name, audience, planned value (PV), earned value (EV), actual cost (AC), decisions or escalations the PM already knows are needed.

### Method

1. Set the overall RAG rating using these rules:
   - **Green:** on track for scope, schedule and budget; no blockers needing help outside the team.
   - **Amber:** at risk; one or more issues could affect a milestone, budget or scope, but there is a credible recovery plan within the team's control.
   - **Red:** a milestone, budget or scope commitment will be missed without intervention, or a blocker needs a decision or support from outside the team.
   - If the user states a status, use it, but flag it if the evidence clearly contradicts it (for example "reported Green, but a blocker has no owner").
2. Give the RAG a one-line reason.
3. For each blocker state the impact (what slips or what it costs) and what is needed to clear it.
4. Milestones go in a table with status per milestone.
5. Budget: report only what the user gave. Do not infer whether spend is healthy unless the user gave the planned percentage or progress to compare against; if not, write "Comparison to plan: Not provided".
6. Earned value: never compute SPI or CPI unless the user gives planned value, earned value and actual cost. If all three are given:
   - SPI = EV / PV (below 1.0 means behind schedule)
   - CPI = EV / AC (below 1.0 means over budget)
   - Show the formula and the numbers. Round to two decimal places.
7. Next steps are actions for the coming week with an owner role.
8. Escalations: list only items that need a decision or help from outside the team. If none, write "None this week".
9. Keep it executive-friendly: short bullets, one page.

### Output skeleton

```
# Weekly Status Report: [Project name or "Not provided"]

**Week ending:** [date or "Not provided"]
**Overall status:** [GREEN/AMBER/RED]
**Reason:** [one line]

## Completed this week
- ...

## In progress
- [Task]: [progress or expected completion, if given]

## Blockers and impact
| Blocker | Impact | Needed to resolve | Owner (role) |
|---|---|---|---|
| [blocker] | [impact] | [action or decision] | [role] |

## Milestones
| Milestone | Due date | Status |
|---|---|---|
| [milestone] | [date or TBC] | [On track/At risk/Delayed/Complete] |

## Budget
- Spent to date: [value or "Not provided"]
- Comparison to plan: [value or "Not provided"]
- Earned value: [SPI = EV / PV = x / y = z; CPI = EV / AC = x / y = z] OR Not calculated (PV, EV and AC not provided)

## Schedule
- [On track/At risk/Delayed]: [one line explanation]

## Next steps
- [Action] (owner: [role])

## Escalations needed
- [Decision or support needed, from whom, by when] OR None this week
```
