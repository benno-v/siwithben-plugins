I would run the routine in read-only mode, write the report and create one unsent email draft addressed only to me@example.com. I'd make no other changes.

**What I would do with tools**

1. **Set the window.** I'd use Monday 00:00 to Friday 14:00 local time. The sample data gives no calendar dates or time zone, so I'd use day names and flag both gaps.
2. **Search email (read only).** I'd search sent and received mail about the Northwind scanner roll-out from this week, which returns Emails 1 to 8.
3. **Read the calendar.** I'd list this week's project events and next week's, which returns 3 meetings held, 1 cancelled and 1 upcoming.
4. **Read the task tool.** I'd export project tasks with owner, due date, status and completion date.
5. **Read meeting notes** from this week: Monday's stand-up and Wednesday's Leeds retrospective.
6. **Check freshness.** All four sources have items from this week, so there are no stale-data warnings.
7. **Create one email draft:**
   - **To:** me@example.com only, with no CC or BCC.
   - **Subject:** `DRAFT status report: Northwind Warehouse Scanner Roll-out, week ending Friday`
   - **Body:** the report below, starting with "DRAFT, not sent".
   
   I would not send it. If it shows up as a card with Send or Discard, I'd leave it for you.
8. **Don't change anything else.** I wouldn't touch any task, event, note or email, and nothing would go to stakeholders.

---

**Output**

[Window: Monday 00:00 to Friday 14:00, local time. The sample data gives no calendar dates or time zone. All sources (email, calendar, task tool, meeting notes) returned items from this week.]

# Northwind Warehouse Scanner Roll-out: Status report, week ending Friday

DRAFT, not sent

**Overall status:** Red: the Bristol go-live next Friday can't go ahead as planned, because the cold store has no usable Wi-Fi and the fix needs a decision from Dana Whitfield, who won't approve option A without a cost that isn't due until next week.

## Summary
Leeds is live, and this week's fixes landed: the 3 faulty batteries were replaced and the duplicate-scan fix reached the test system. Bristol's Wi-Fi survey found no usable coverage in cold store aisles 14 to 22, which puts next Friday's go-live at risk. We need a sponsor decision on option A (a two-week delay plus new access points) or option B (go live without the cold store) by next Tuesday.

## Done this week
- Bristol Wi-Fi survey completed (Tuesday).
- 3 faulty scanner batteries replaced at Leeds (Thursday).
- Bristol training sessions 1 and 2 delivered for the day and twilight shifts (Thursday).
- Duplicate-scan fix deployed to the test system (Friday).

## In progress
- Bristol training sessions 3 and 4 (night shift and cold store team), owner: Maria Santos, expected: next Wednesday
- Bristol go-live readiness checklist, owner: Priya Nair, expected: next Thursday
- User acceptance testing (UAT) of the duplicate-scan fix, owner: Not provided, expected: next Thursday
- Night-shift battery feedback, owner: Lee Okafor, expected: next Wednesday
- **Overdue:** update the scanner user guide with the cold-store procedure, owner: Maria Santos, was due Tuesday, not started. Maria will pick it up after the training sessions.

## Blockers and risks
- **Blocker:** no usable Wi-Fi in the Bristol cold store (aisles 14 to 22). Impact: the cold store can't go live, and next Friday's Bristol go-live is at risk. Action: Dana Whitfield to choose option A or B by next Tuesday. A decision call is set for Monday 09:00. Jordan Ellis is getting the access point cost, but it won't arrive before next week.
- **Risk:** UAT of the duplicate-scan fix has no owner. Impact: the fix can't reach production by the end of next week. Action: Sam Taylor to name a Leeds tester.
- **Risk:** night-shift users report low batteries before the end of the shift on older units. Impact: scanner availability on nights. Action: Lee Okafor to collect feedback by next Wednesday.
- **Risk:** the user guide update is overdue. Impact: the cold-store procedure isn't documented ahead of go-live. Action: Maria Santos, after the training sessions.

## Upcoming milestones
| Milestone | Due | Confidence |
|---|---|---|
| Bristol go-live | Next Friday | Low |
| Duplicate-scan fix in production | End of next week, if UAT passes | Medium |
| Glasgow go-live | Not provided | Not provided |

## Budget and schedule
- Budget: Not provided. Budget wasn't discussed this week, and the cost of the extra access points isn't quoted yet. The access points are outside the current scope.
- Schedule: At risk. The Bristol cold store can't go live without a decision on option A (two-week delay) or option B (partial go-live).

## Decisions or help needed
- Dana Whitfield: choose option A or option B for Bristol by next Tuesday. This will be discussed on the Monday 09:00 decision call.
- Dana Whitfield: agree the Glasgow go-live date. No date has been set.

## Next steps
- Monday: decision call on the Bristol cold store options (Sam Taylor, Dana Whitfield, Priya Nair).
- Jordan Ellis to get the access point cost from the network supplier.
- Maria Santos to run training sessions 3 and 4 on Tuesday and Wednesday, then update the user guide.
- Name a UAT owner at Leeds and complete UAT by Thursday.
- Priya Nair to finish the readiness checklist by Thursday.

Sources
- Done: Wi-Fi survey: Task: Bristol Wi-Fi survey / Email: Priya Nair, Tuesday, "Bristol Wi-Fi survey: problem in the cold store"
- Done: batteries: Task: Replace 3 faulty scanner batteries at Leeds / Email: Kim Ashby, Tuesday, "RE: Replacement batteries…"
- Done: training 1 and 2: Task: Bristol training sessions 1 and 2 / Email: Maria Santos, Thursday, "Bristol training update"
- Done: fix to test: Task: Deploy duplicate-scan fix to test / Email: Chris Dube, Friday, "Duplicate scan fix is on the test system"
- In progress: training 3 and 4: Task: Bristol training sessions 3 and 4 / Email: Maria Santos, Thursday
- In progress: readiness checklist: Task: Bristol go-live readiness checklist
- In progress: UAT: Task: UAT of duplicate-scan fix / Notes: Leeds pilot retrospective, Wednesday
- In progress: battery feedback: Notes: Leeds pilot retrospective, Wednesday
- Overdue: user guide: Task: Update scanner user guide… / Email: Maria Santos, Thursday
- Blocker: cold store Wi-Fi: Email: Priya Nair, Tuesday / Email: Sam Taylor, Wednesday, "Decision needed: Bristol go-live…" / Email: Dana Whitfield, Thursday, "RE: Decision needed…" / Meeting: Decision call, next Monday
- Risk: night-shift batteries: Notes: Leeds pilot retrospective, Wednesday
- Milestones: Task: Bristol go-live / Email: Chris Dube, Friday / Task: Glasgow go-live / Notes: Weekly stand-up, Monday
- Budget: Notes: Weekly stand-up, Monday / Email: Priya Nair, Tuesday / Email: Sam Taylor, Wednesday
- Decisions: Email: Sam Taylor, Wednesday / Email: Dana Whitfield, Thursday / Notes: Weekly stand-up, Monday
- Steering check-in cancelled: Meeting: Steering check-in, Thursday (cancelled by Dana Whitfield)

Missing data
- Budget position: no figure in any source. It would normally come from the project tracker or the sponsor.
- Access point cost: Jordan Ellis is getting a quote from the network supplier, due next week.
- UAT owner for the duplicate-scan fix: not assigned in the task tool or the retrospective notes.
- Glasgow go-live date: not recorded in the task tool. It is to be agreed with Dana Whitfield.
- Calendar dates and time zone for the reporting window: not in the evidence, so day names are used.

---

**Validation**
- Every owner and date traces to a named source, and gaps say "Not provided".
- The report gives no budget figure or percentage. The Leeds counts (42 of 45 in use) are left out because the batteries were replaced this week.
- The Leeds pilot go-live is left out of Done because it was completed last week.
- The Red rating matches the blocker, which needs a decision from the sponsor.
- The report is labelled "DRAFT, not sent", and the only draft is addressed to me@example.com and has not been sent.
