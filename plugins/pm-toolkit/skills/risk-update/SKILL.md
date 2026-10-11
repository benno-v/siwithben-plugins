---
name: risk-update
description: Check a project's risk register against recent updates (notes the user gives, or recent status reports/meeting notes) and recommend line-by-line changes to status, score and notes. Always verifies a risk ID against its description before editing, and never edits the file silently. Use when the user asks to update, review or refresh a risk register, close out a risk, or change a specific risk by ID.
---

# Risk update

Review a project's existing risk register against what has actually happened recently, and propose changes — status, score, notes — one risk at a time. This skill does not write a register from scratch (use `/pm-toolkit:risk-register` for that); it updates one that already exists.

## Ground rules

- Work only from what the user gives you (notes, pasted updates) or recent documents you can read in the connected folder (status reports, meeting notes). Never invent a risk, score, status or note.
- **Never edit the risk register file without the user confirming the change first.** Propose changes, show them clearly, and only write them once the user says to go ahead.
- **Before changing any risk by ID, verify the ID against its description.** Read the risk register, find that ID, and check the description the user gave matches what the register actually says for that ID. If it does not match (or no clear match exists), stop: tell the user what the register actually shows for that ID, search the register for the risk description they described, and if you find a better match, name that ID and ask the user to confirm before doing anything. Do not edit based on an assumed ID.
- When you do edit the register file, preserve its existing format exactly (same table structure, same columns, same markdown/CSV style) — only change the cells that need to change.
- Plain business English, short notes, no jargon.

## Inputs to look for

The existing risk register (read from the connected folder, or pasted by the user), and whatever is prompting the update: specific instructions from the user ("set risk 002 to mitigating because..."), or recent status reports/meeting notes that mention risks changing. If neither is available, ask once what should drive the update.

## Method

1. Read the current risk register in full before proposing anything.
2. If the user named a specific risk ID and gave a description or reason, look up that ID in the register and compare its stored description to what the user said:
   - If it's a clear match, proceed.
   - If it does not match, do **not** edit. Report: "Risk <ID> in the register is '<actual description>', which doesn't match what you described ('<user's description>')." Then scan the register for a risk whose description does match what the user described, and if found say: "Risk <other ID> looks like the one you mean: '<its description>'. Confirm and I'll update that one instead." If no match is found, ask the user to point to the right risk.
3. For updates driven by status reports/meeting notes rather than a specific ID, go risk by risk: flag any risk whose status, likelihood or impact looks out of date given what the documents now say, and propose a specific change with a reason.
4. For each proposed change, show: risk ID, what changes (status / L / I / Score / notes), the new value, and the source (user's words or the document) that justifies it.
5. Only after the user confirms (explicitly, or by saying something like "yes, do it" / "update it"), edit the register file, keeping its existing structure and formatting intact. Recalculate Score (L × I) if L or I changed.
6. If a risk is now closed/resolved, propose moving its status to Closed with a closure note rather than deleting the row — never delete rows without being asked to.

## Output format (for the proposal, before any edit)

```
# Risk register review: <Project name or "Not provided">
Register reviewed: <file> · Driven by: <user notes / source file(s)>

## Proposed changes
| ID | Field | Current | Proposed | Reason / source |
|---|---|---|---|---|
| R.. | Status | ... | ... | ... |

## ID checks
- <only if a mismatch was found> "Risk <ID> you mentioned is actually '<description>' in the register, not '<what you described>'. Did you mean <other ID>: '<description>'?"

## Not changing
- <risks reviewed but left as-is, briefly why>
```

After the user confirms, apply the edits to the file and report back with a short "Updated: <ID list>" line, still referencing the same table above so the user can see exactly what changed.

## Before handing over

Add one line: "I only update the register when you confirm — check the proposed changes above before I touch the file, especially any risk ID I flagged as a possible mismatch."
