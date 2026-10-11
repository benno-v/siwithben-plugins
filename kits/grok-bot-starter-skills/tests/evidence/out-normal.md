[Window: this Monday 00:00 to today, Friday 14:00, local time. The sources don't give calendar dates or a time zone, so dates below are relative to this week. All four sources returned items from this week: email (8 messages), calendar (4 meetings this week, plus 1 next week), task tool (11 tasks) and meeting notes (2 notes). The task tool also lists one item completed last Monday, "Leeds pilot go-live", which is not counted as done this week.]

# Northwind Warehouse Scanner Roll-out: Status report, week ending Friday (this week)

DRAFT, not sent

**Overall status:** Red: The Bristol go-live next Friday can't go ahead as planned because there's no usable Wi-Fi in the cold store, and it needs a sponsor decision between option A and option B that is still open.

## Summary
The Leeds pilot is running, with 42 of 45 scanners in daily use at the start of the week. Replacement batteries for the other 3 have been fitted, and Contoso has deployed a fix for duplicate scans to the test system. Bristol training is on track, but the Wi-Fi survey found no usable coverage in the cold store (aisles 14 to 22), so the go-live depends on a decision from Dana Whitfield by next Tuesday.

## Done this week
- Bristol Wi-Fi survey completed (Jordan Ellis and Priya Nair, this Tuesday). It found no usable coverage in cold store aisles 14 to 22.
- 3 replacement scanner batteries fitted at Leeds under warranty from Fabrikam (Lee Okafor, yesterday).
- Bristol training sessions 1 and 2 delivered for the day and twilight shifts (Maria Santos, yesterday).
- Duplicate-scan fix deployed to the test system (Chris Dube, Contoso, today).
- Decision request on Bristol cold store options sent to the sponsor (Sam Taylor, this Wednesday).

## In progress
- Bristol training sessions 3 and 4 (night shift and cold store team), owner: Maria Santos, expected: next Wednesday
- Bristol go-live readiness checklist, owner: Priya Nair, expected: next Thursday
- User acceptance testing (UAT) of the duplicate-scan fix, owner: Not provided, expected: next Thursday
- **Overdue:** Update the scanner user guide with the cold-store procedure. Owner: Maria Santos. It was due this Tuesday and is not started. Expected: Not provided (Maria says she will pick it up after training sessions 3 and 4).
- Night-shift battery feedback on older units, owner: Lee Okafor, expected: next Wednesday

## Blockers and risks
- **Blocker:** There is no usable Wi-Fi in the Bristol cold store, aisles 14 to 22. Impact: the cold store can't go live next Friday as things stand, and extra access points weren't in the project scope. Action: Dana Whitfield to choose option A or option B. She needs to decide by next Tuesday, and a decision call is booked for next Monday at 09:00.
  - Option A is a two-week delay to add access points. Its cost hasn't been quoted.
  - Option B is to go live next Friday everywhere except the cold store, which keeps the old scanners.
- **Risk:** Dana won't approve option A without seeing the cost. Jordan Ellis is getting a quote from the network supplier, but it won't arrive before next week. Impact: the decision may not be fully informed by next Tuesday. Action: Jordan Ellis to obtain the quote.
- **Risk:** Nobody owns UAT of the duplicate-scan fix. Impact: putting the fix into production by the end of next week depends on someone at Leeds who knows the picking flow passing UAT. Action: owner to be confirmed (Not provided).
- **Risk:** The user guide's cold-store procedure is overdue, and the cold store team is due to be trained next Wednesday. Action: Maria Santos to update the guide after the sessions.
- **Risk:** The Leeds night shift reports that batteries run low before the end of the shift on older units. Action: Lee Okafor to collect feedback by next Wednesday.
- **Risk:** The steering check-in with Dana was cancelled yesterday, so the decision moved to next Monday.

## Upcoming milestones
| Milestone | Due | Confidence |
|---|---|---|
| Sponsor decision on the Bristol cold store (option A or B) | Next Tuesday | Medium |
| Bristol go-live readiness checklist | Next Thursday | Medium |
| UAT of duplicate-scan fix | Next Thursday | Low |
| Bristol go-live | Next Friday | Low |
| Duplicate-scan fix into production | End of next week (if UAT passes) | Low |
| Glasgow go-live | Not provided | Low |

## Budget and schedule
- Budget: Not provided. Budget wasn't discussed at this week's stand-up, and the cost of the cold store access points, which are outside the current scope, hasn't been quoted yet.
- Schedule: At risk. The Bristol go-live next Friday depends on the cold store decision, and option A would delay it by two weeks. The Glasgow go-live date hasn't been agreed.

## Decisions or help needed
- Dana Whitfield: choose option A (delay plus access points) or option B (go live next Friday without the cold store), by next Tuesday. Discussion is scheduled for next Monday at 09:00.
- Dana Whitfield: agree the Glasgow go-live date (by when: Not provided).

## Next steps
- Monday 09:00: decision call on the Bristol cold store options (Sam Taylor, Dana Whitfield, Priya Nair).
- Jordan Ellis: get the access point cost from the network supplier.
- Maria Santos: run Bristol training sessions 3 and 4 next Tuesday and Wednesday, then update the user guide.
- Priya Nair: complete the Bristol go-live readiness checklist by next Thursday.
- Confirm a Leeds UAT owner and complete UAT of the duplicate-scan fix by next Thursday.
- Lee Okafor: collect night-shift battery feedback by next Wednesday.

Sources
- [Status, Summary, Blocker] Bristol cold store Wi-Fi: Email: Priya Nair, this Tuesday, "Bristol Wi-Fi survey: problem in the cold store"; Meeting: Bristol Wi-Fi survey walk-through, this Tuesday
- [Blocker, Decisions] Options A and B, decision by next Tuesday: Email: Sam Taylor to Dana Whitfield, this Wednesday, "Decision needed: Bristol go-live and cold store Wi-Fi"
- [Risks, Decisions] Dana needs the option A cost, discussion on Monday: Email: Dana Whitfield, yesterday, "RE: Decision needed…"
- [Risks] Steering check-in cancelled: Meeting: Steering check-in: scanner roll-out, yesterday (cancelled)
- [Next steps, Decisions] Decision call next Monday 09:00: Meeting: Decision call: Bristol cold store options, next Monday
- [Summary] 42 of 45 Leeds scanners in use: Email: Lee Okafor, this Monday, "Leeds pilot: end of week 1"
- [Done] Wi-Fi survey: Task: Bristol Wi-Fi survey
- [Done] Batteries replaced: Task: Replace 3 faulty scanner batteries at Leeds; Email: Kim Ashby, this Tuesday, "RE: Replacement batteries…"; Email: Sam Taylor, this Monday, "Replacement batteries…"
- [Done] Training sessions 1 and 2: Task: Bristol training sessions 1 and 2; Email: Maria Santos, yesterday, "Bristol training update"
- [Done] Duplicate-scan fix on test: Task: Deploy duplicate-scan fix to test; Email: Chris Dube, today, "Duplicate scan fix is on the test system"
- [In progress] Training sessions 3 and 4: Task: Bristol training sessions 3 and 4; Email: Maria Santos, yesterday
- [In progress] Readiness checklist: Task: Bristol go-live readiness checklist
- [In progress, Risks] UAT with no owner: Task: UAT of duplicate-scan fix; Notes: Leeds pilot retrospective, this Wednesday; Email: Chris Dube, today
- [In progress, Risks] User guide overdue: Task: Update scanner user guide with cold-store procedure; Email: Maria Santos, yesterday
- [In progress, Risks] Night-shift batteries: Notes: Leeds pilot retrospective, this Wednesday
- [Milestones] Bristol go-live next Friday: Task: Bristol go-live; Notes: Weekly stand-up, this Monday
- [Milestones, Decisions] Glasgow date not agreed: Task: Glasgow go-live; Notes: Weekly stand-up, this Monday
- [Budget] Budget not discussed, access point cost unquoted: Notes: Weekly stand-up, this Monday; Email: Priya Nair, this Tuesday

Missing data
- Budget position: no figure in any source. It would normally come from the steering check-in or the project tracker.
- Cost of the extra cold store access points: not yet quoted. It will come from Jordan Ellis via the network supplier next week.
- Owner for UAT of the duplicate-scan fix: missing in the task tool and in the retrospective notes ("Owner to be confirmed").
- Glasgow go-live date: missing in the task tool and still to be agreed with Dana.
- New expected date for the overdue user guide update: missing in the task tool and in Maria's email.
- Confidence ratings for milestones aren't stated in any source. They are the report's own assessment of the evidence above.
- Calendar dates and time zone for the reporting window aren't given in the sources.
