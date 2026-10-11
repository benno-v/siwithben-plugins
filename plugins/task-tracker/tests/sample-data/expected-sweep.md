# Expected sweep result for the sample data

What a good sweep of this folder finds, so you can check the `sweep` skill against it. Reference date: Monday 2026-10-12, last sweep 2026-10-05 08:00. `sweep-changes.json` is the block the sweep writes after you approve everything below (interactive mode).

## New tasks, committed (Open after approval)

| New ID | Action | Owner | Due | Sources | Why it counts |
|---|---|---|---|---|---|
| T-009 | Send signed purchase order to procurement | Mei Chen | 2026-10-14 | Gmail email 5, Slack thread 1, weekly check-in | "I'll send ... by Wednesday 14 October". **Duplicate across three sources, merged into one row** |
| T-010 | Set up UAT environment | Tom Becker | 2026-10-19 | ClickUp CP-121 | Assigned in the PM tool |
| T-011 | Write go-live comms plan | Alex Morgan | 2026-10-20 | ClickUp CP-124, weekly check-in | "agreed Alex to write". **Duplicate across two sources, merged** |
| T-012 | Rotate the admin passwords before UAT starts | Tom Becker | blank | Security review notes | "I'll rotate". Due date is vague ("before UAT starts"), so it stays blank with a note |

## New tasks, proposed (need your approval)

| New ID | Action | Why it needs you |
|---|---|---|
| T-013 | Book the accessibility auditor before go-live | **Ambiguous owner:** Sam Taylor and Jordan Lee in one message, "one of you will need to". Jordan's "happy to help" is not a clear commitment |
| T-014 | Check the data migration test results with the vendor | **Ambiguous owner:** "Priya and Tom ... one of them will check". Due "before Friday" read as Fri 2026-10-09 from the meeting date |

## Merged into existing rows (no new task)

- T-003 Send updated Q4 budget forecast to finance: Gmail email 1 asks for the same thing ("by Monday" = 2026-10-12). **Duplicate of an existing row**; the new email is added to the Source column. Owner and due unchanged.

## Suggested updates (shown, never applied silently)

- T-005 Draft FAQ: due 2026-10-23 to 2026-10-21 (ClickUp CP-118 activity, 2026-10-09).

## Probably done (confirm before marking)

- T-001 Send revised returns policy wording to legal: Gmail email 4 from Priya Nair, "here is the revised returns policy wording (attached)", 2026-10-09.

## Not tracked: passing remarks (4)

- "It would be nice to add a chatbot to the portal at some point" (Gmail email 3, Jordan Lee)
- "we should probably redo the onboarding emails at some point" (Slack thread 1, Jordan Lee)
- "Might be worth looking at single sign-on later too" (Slack thread 1, Tom Becker)
- "it would be nice to have a small launch event" (weekly check-in)

## Information only

- Gmail email 2: Contoso will confirm the go-live date by Friday 16 October. Supports T-004 (Waiting); no change.
- Gmail email 6: office closed Monday 19 October. No action.
- Calendar: four events, no new actions. The vendor call (Tue 13 Oct) relates to T-004; the training session (Wed 14 Oct) relates to T-002.

## Scheduled mode (Proposed only)

Run on a schedule, the same sweep adds all six new tasks to "Proposed, needs approval", updates Last sweep and lists the merge, suggested update and probably-done items in its report without changing those rows.
