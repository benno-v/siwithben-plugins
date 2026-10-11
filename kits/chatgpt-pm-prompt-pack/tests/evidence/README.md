# Test evidence (11 Oct 2026)

I ran each sample input from `../sample-inputs.md` through a stand-in model (Cursor Agent, ask mode) given `gpt/instructions.md` plus `gpt/knowledge/pm-templates.md`, then checked the output against the template. ChatGPT itself may phrase things differently; the formats are what I check.

| Test | Result |
|---|---|
| 1 Charter | Asked once for sponsor, budget, baseline figures, dates and scope (test1). After "Just draft it" (test1b) it produced all ten sections, marked gaps "Not provided"/"TBC", and listed GDPR as a constraint and the DPO as a stakeholder. |
| 2 WBS + PERT | 27 tasks. A script recomputed E = (O+4M+P)/6 for every row (0 mismatches); E totals 400.0 hours, which matches the summary; the by-role table adds up; E ± 2SD is shown. |
| 3 Risk register | 10 risks across categories. A script checked every score = P × I and its band (0 mismatches); the table pastes into Excel. |
| 4 Exec translator | 5 bullets, business impact, USD 12,000 and timeline stated, exactly one decision. |
| 5 Weekly status | RAG with reason, milestones table, 62% spent kept as given, earned value "Not calculated" because PV/EV/AC weren't supplied, escalation named. |
| Plain prompt 4 (prompt-pack.md, no GPT) | On an update with no decision needed, it correctly wrote "Decision needed: No decision needed". |
