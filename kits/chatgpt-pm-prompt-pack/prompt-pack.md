# PM Prompt Pack: 5 copy-paste prompts

*By Benjamin Vermeulen, SI with Ben ([@SIwithBen](https://www.youtube.com/@SIwithBen))*

These are the plain-prompt versions of my PM Prompt Pack GPT. You don't need to build a GPT or have a paid plan: copy a prompt into ChatGPT (free plan is fine), or any other AI assistant, fill in the placeholders and send it.

## How to use

1. Pick the prompt that matches the job: charter, WBS and estimates, risks, executive summary or weekly status.
2. Copy everything inside the grey box.
3. Replace every [PLACEHOLDER] with your own details. If you don't know something, write "Not provided" and the assistant will mark the gap rather than guess.
4. Send it, then iterate: ask it to tighten one section, change the audience, or turn a table into a CSV for Excel.
5. Don't paste confidential client or personal data unless your workspace policy allows it. Anonymise names and figures if you're unsure.

**Always review the output.** It's a first draft. You are the final quality gate for accuracy, numbers and tone.

---

## Prompt 1: Project Charter

```
Act as an experienced project manager working in line with PMBOK practice. Create a project charter for [PROJECT NAME].

Project context: [2 TO 3 SENTENCES: WHAT THE PROJECT IS AND WHY NOW]
Sponsor (role): [ROLE]
Timeframe: [TIMEFRAME OR DEADLINE]
Budget: [BUDGET OR "Not provided"]
Known constraints: [CONSTRAINTS OR "Not provided"]

Include these sections in this order:
1. Purpose (the business problem or opportunity)
2. Objectives in SMART format (3 to 5, each with a measure and a date)
3. Scope: in scope and out of scope
4. Stakeholders: primary, secondary and external
5. High-level requirements
6. Constraints
7. Assumptions to validate (and who should validate each)
8. Success criteria
9. Key milestones as a table: Milestone | Target date | Owner (role)

Rules:
- Keep it under 2 pages. Use bullet points for clarity.
- Do not invent figures, dates, names or budgets. Mark missing items "Not provided" and open decisions "TBC".
- Use roles, not personal names, for owners.
- Use British spelling and plain business English.
```

---

## Prompt 2: WBS and Three-Point (PERT) Estimation

```
Act as an experienced project manager. Break down this project requirement into a work breakdown structure with three-point estimates.

Requirement: [PASTE REQUIREMENT]
Team roles available: [ROLES, FOR EXAMPLE DEVELOPER, DESIGNER, QA]
Constraints: [DEADLINE, TECHNOLOGY, TEAM SIZE OR "Not provided"]

Output:
1. An indented WBS with numbered levels (1, 1.1, 1.1.1). Include project management, testing and deployment work.
2. A table with these columns: ID | Task | Hours (O) | Hours (M) | Hours (P) | Hours (E) | SD | Depends on | Skills / role | Key risk
   - O = optimistic, M = most likely, P = pessimistic, in effort hours.
   - E = (O + 4M + P) / 6 and SD = (P - O) / 6 for each task.
3. A summary with total E, total SD (square root of the sum of SD squared) and a confidence range of E plus or minus 2 SD. Show the formulas.
4. An effort-by-role table: Role | Tasks | Hours (E) | Share of total.

Rules:
- Label all estimates as planning estimates for the team to validate.
- Keep tables simple, one value per cell, so they paste into Excel.
- Use British spelling and plain business English.
```

---

## Prompt 3: Risk Identification and Register

```
Act as an experienced project manager. Identify the top [NUMBER, DEFAULT 10] risks for a [PROJECT TYPE] project in [INDUSTRY].

Project specifics: [SCOPE, TIMEFRAME, BUDGET, TEAM, KEY DEPENDENCIES]

Cover four categories: technical, external, organisational and project management.

Format as a table for Excel with these columns:
ID | Category | Risk description | Probability (H/M/L) | Impact (H/M/L) | Score (1-9) | Rating | Mitigation | Owner (role)

Rules:
- Write each risk as cause, event, effect, specific to this project.
- Score: H = 3, M = 2, L = 1. Score = probability x impact. 6 to 9 High, 3 to 4 Medium, 1 to 2 Low.
- Sort by score, highest first.
- Mitigation is a concrete action starting with a verb. Owner is a role, not a name.
- After the table, list the top 3 risks to discuss with the sponsor, one line each.
- Use British spelling and plain business English.
```

Tip: stick to around 10 risks per request. When I ask for 30 at once, quality drops and the list gets generic. Do a second pass on one category instead.

---

## Prompt 4: Communication (Executive) Translator

```
Translate this technical project update into an executive summary for [AUDIENCE, FOR EXAMPLE THE SPONSOR OR BOARD].

Technical update: [PASTE TECHNICAL UPDATE]

Requirements:
- 3 to 5 bullet points maximum.
- Focus on business impact (customers, revenue, operations, compliance), not technical detail. Explain any unavoidable jargon in a few words.
- Include timeline and budget implications. Use only figures in the update; if an impact is unknown, say "not yet quantified".
- End with "Decision needed:" followed by exactly one decision, only if the update genuinely needs one. Otherwise write "Decision needed: No decision needed".
- Professional but conversational tone. No blame.
- Use British spelling and plain business English.
```

---

## Prompt 5: Weekly Status Report

```
Generate an executive-friendly weekly project status report from these inputs.

Project: [PROJECT NAME]
Week ending: [DATE]
Tasks completed: [LIST]
Tasks in progress: [LIST]
Blockers: [LIST]
Upcoming milestones: [LIST WITH DATES]
Budget status: [PERCENTAGE SPENT, AND PLANNED PERCENTAGE IF KNOWN]
Schedule status: [ON TRACK / AT RISK / DELAYED]
Earned value (optional): PV [VALUE], EV [VALUE], AC [VALUE]

Sections in this order:
1. Overall RAG status with a one-line reason
2. Completed this week
3. In progress
4. Blockers and impact (table: Blocker | Impact | Needed to resolve | Owner (role))
5. Milestones (table: Milestone | Due date | Status)
6. Budget
7. Schedule
8. Next steps (with owner role)
9. Escalations needed (or "None this week")

RAG rules:
- Green: on track for scope, schedule and budget; no blockers needing outside help.
- Amber: at risk, but a credible recovery plan is within the team's control.
- Red: a commitment will be missed without intervention, or a blocker needs a decision from outside the team.

Rules:
- Only calculate SPI and CPI if PV, EV and AC are all given. If so, show SPI = EV / PV and CPI = EV / AC with the numbers.
- Do not invent figures. Mark missing items "Not provided".
- Keep it to one page. Use British spelling and plain business English.
```

---

## Before you share anything

Review before sharing: this is an AI draft and you are the final quality gate for accuracy, numbers and tone.

More on my channel: [youtube.com/@SIwithBen](https://www.youtube.com/@SIwithBen)
