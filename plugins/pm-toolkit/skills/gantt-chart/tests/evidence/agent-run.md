## Gantt chart ready: Project plan
2 November 2026 to 1 December 2026, durations in calendar days.

**Files**
- HTML: `/tmp/tmp.EFqV1LdoqN/project-plan-gantt.html`
- Excel: `/tmp/tmp.EFqV1LdoqN/project-plan-gantt.xlsx`
- PowerPoint: `/tmp/tmp.EFqV1LdoqN/project-plan-gantt.pptx`
- Task list (normalised): `/tmp/tmp.EFqV1LdoqN/project-plan-tasks.json`

**On the chart:** 4 of 5 tasks, 1 milestone. Requirements was worked out from its dependency and runs from 4 to 8 November.

**Critical path:** T5 Go-live (1 task with zero float). This is only partial. Build depends on Design, and Design has no dates, so the script cannot trace the path back through Build. Once Design has dates, the critical path should run through Design, Build and Go-live.

**Unscheduled, needs dates (1)**
| ID | Task | What is missing |
|---|---|---|
| T3 | Design | No start date, end date, duration or dependency |

**Checks (1)**
- T5 Go-live has no owner.

**Assumptions:**
- You didn't say whether to count calendar days or working days, so I used calendar days.
- All dates were in ISO format (YYYY-MM-DD), so the date format wasn't in doubt.
- I read "5 days after kick-off" as a 5-day task that starts the day after Kick-off ends. That gives 4 to 8 November. If you meant it starts 5 days after Kick-off, tell me and I'll change it.
- You didn't give a plan name, so I used "Project plan".
- I saved the files in the current folder because there is no `outputs/` folder.

**Questions**
1. Should durations be calendar days or working days?
2. What dates or duration does Design have? Build starts on 16 November, so Design would need to finish by 15 November.
3. Who owns Go-live?
4. Is "Project plan" the right name?

Nothing was sent or uploaded. Check the dates, owners and dependencies with the people doing the work, fill the gaps above, then run the chart again.
project-plan-gantt.html
project-plan-gantt.pptx
project-plan-gantt.xlsx
project-plan-tasks.json
