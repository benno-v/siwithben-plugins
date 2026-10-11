---
name: weekly-status-report
description: Use when I ask for a weekly status report, project update or end-of-week summary for a project, or when the weekly status report routine runs.
---

# Weekly status report

Gather this week's evidence for a project from my connected tools and draft a one-page status report in a fixed format with an overall Green, Amber or Red rating. Every line traces back to a source. Return it to me as a draft; never send, post or share it.

## When to use

- I ask for a "status report", "weekly update", "project update", "end-of-week summary" or "what happened on [project] this week".
- The weekly status report routine runs (see the ROUTINE section below).

## Inputs and access

- **Project or projects.** The name, plus anything that identifies it in my tools (a Notion database, a label, a channel, key people).
- **Reporting week:** Monday 00:00 to now, in my time zone. The week ending date is today's date.
- **Sources, whichever are connected (read access only):**
  - **Email** (for example Gmail): sent and received messages about the project.
  - **Calendar:** project meetings held this week and those coming up next week.
  - **Task tool** (for example Notion): tasks done this week, in progress, overdue and due next week.
  - **Meeting notes:** wherever I keep them (for example Notion pages or shared documents).

In a one-off run, if I haven't said which project or which sources, ask me once in a single short message, then continue with what I tell you. In routine mode, don't ask: use the project and sources written in the routine instructions, and note anything you couldn't reach.

If none of the named sources can be reached, stop and tell me in one line. Don't write a report from memory or an earlier run.

## Sequence of work

1. **Set the window.** Work out Monday 00:00 to now in my time zone and state it at the top.
2. **Gather evidence** from each source, limited to the project and the window:
   - Email: decisions, requests, problems, dates and commitments, in both directions.
   - Calendar: meetings held this week (and any cancelled), plus project meetings and deadlines next week.
   - Task tool: tasks completed this week, in progress, overdue (due before today and not done) and due next week, with owner and due date as recorded.
   - Meeting notes: decisions, actions with owners and dates, risks raised.
3. **Check freshness.** For each source, note whether it returned anything from this week. Apply the stale and no-data rules below.
4. **Sort the evidence** into the report sections. Count something as done this week only if it was completed in the window; work finished last week is not news.
5. **Decide the overall status** using these rules, with a one-sentence reason:
   - **Green:** on track for scope, time and budget; no blocker needs escalation.
   - **Amber:** at least one milestone or the budget is at risk, but the team has a recovery plan it can run itself.
   - **Red:** a milestone will be missed or the budget exceeded without a decision or help from the reader.
   If the sources already state a status, keep it, but say briefly if the evidence points elsewhere.
6. **Fill gaps honestly.** Write "Not provided" for any missing owner, date, milestone, budget or schedule position, and add each one to the Missing data list. Never compute a percentage, total or trend that isn't stated in the sources.
7. **Write the report** in the exact structure under What to return, then the Sources and Missing data lists.
8. **Validate** using the checklist below, then return the report in this conversation.

## Approval rules

- **Never send, post, publish or share** the report, or any part of it, to anyone. Return it in this conversation, labelled as a draft.
- **Send to me only (optional variant).** Only if I explicitly ask for "send to me only", or the routine says so, you may create one email draft addressed to me and nobody else, with the subject `DRAFT status report: [project], week ending [date]` and the report as the body, starting with `DRAFT, not sent`. No other recipients, no CC, no BCC. Create the draft only; never send it.
- Don't create, edit, complete, reassign or re-date tasks, notes, calendar events or emails.
- Anything that reaches someone other than me (an email to stakeholders, a post in a channel, a shared page) needs my explicit approval in this conversation, for that specific report and those specific recipients. Approval for one week doesn't carry over to the next.
- If drafts arrive as draft cards with Send or Discard, leave them for me to act on.

## How to validate before returning

- Every owner and date in the report traces to a named source. Anything else says "Not provided".
- No budget figure, percentage or total appears unless a source states it.
- "Done this week" contains only items completed in the reporting window.
- The RAG reason matches the Blockers and risks section: a blocker that needs a decision from the reader means Red, a risk with a team-owned recovery plan means Amber, no escalation means Green.
- Every bullet in the report appears in the Sources list, and every gap appears in Missing data.
- The report is labelled `DRAFT, not sent`. Nothing has been sent, posted or shared, and no draft is addressed to anyone except me.

## What to return

Use exactly this structure and these headings. Keep the report to one page, in plain business language.

```
[Window: Monday [date] 00:00 to [date and time], [time zone]. Any source or freshness warnings go here.]

# [Project name]: Status report, week ending [date]

DRAFT, not sent

**Overall status:** [Green | Amber | Red]: [one-sentence reason]

## Summary
[2 to 3 sentences a busy executive can read in 15 seconds.]

## Done this week
- [item]

## In progress
- [item], owner: [name or "Not provided"], expected: [date or "Not provided"]

## Blockers and risks
- [issue], [impact], [action and owner]

## Upcoming milestones
| Milestone | Due | Confidence |
|---|---|---|
| [milestone] | [date or "Not provided"] | [High / Medium / Low] |

## Budget and schedule
- Budget: [position from the sources, or "Not provided"]
- Schedule: [On track / At risk / Delayed, with the reason, or "Not provided"]

## Decisions or help needed
- [a clear ask, with who and by when] (or "None this week")

## Next steps
- [what happens next week]

Sources
- [Section] [bullet, shortened]: [Email: sender, date, subject / Meeting: title, date / Task: name / Notes: title, date]

Missing data
- [what's missing and where it would normally come from] (or "None")
```

If I asked for more than one project, return one report per project, each with its own Sources and Missing data lists.

## Stale or missing data

- **A source returns nothing for this week,** or its newest item is older than Monday of the reporting week: say so at the top (for example "Task tool: no updates since last Thursday"). Don't fill the gap with older data, and add it to Missing data.
- **A source isn't connected or access is denied:** say so in one line at the top and carry on with the others.
- **Nothing from any source this week:** don't write a report. Reply with one line saying no project activity was found for the week and which sources were checked.
- **Conflicting evidence** (for example a task marked done but an email saying it isn't): report both under Blockers and risks and list the conflict in Missing data. Don't pick one.

## ROUTINE

Suggested schedule: Fridays at 14:00, which leaves time to review the draft before the end of the week. Paste this into a chat with the Bot that should own the routine and change the bits in square brackets.

```
Every Friday at 14:00 (my time zone: [your time zone, e.g. Europe/London]), run the /weekly-status-report skill for [project name]. Use evidence from Monday 00:00 to now in my time zone, from these sources: my email (sent and received), my calendar, [my Notion project tracker or other task tool] and meeting notes in [where you keep them]. Write the report in the skill's fixed format, labelled "DRAFT, not sent", with an overall Green, Amber or Red status, a Sources list and a Missing data list. Write "Not provided" for anything you can't find; never invent owners, dates, milestones, budget figures or percentages, and never fill a gap with data from before this week. Return the report here in this conversation only. Never send, post or share it, and don't create drafts to anyone. If a source is unavailable or has nothing from this week, say so at the top. Show me the next run time before saving the routine.
```

Optional "send to me only" variant, if you'd like the draft waiting in your mailbox as well:

```
Every Friday at 14:00 (my time zone: [your time zone, e.g. Europe/London]), run the /weekly-status-report skill for [project name], using the same sources and rules as above. Return the report here in this conversation. Then create one email draft addressed only to me ([your email address]) with the subject "DRAFT status report: [project name], week ending [date]" and the report as the body, starting with "DRAFT, not sent". No other recipients, no CC, no BCC. Never send the draft and never send the report to stakeholders; I'll review it and decide who gets it. If a source is unavailable or has nothing from this week, say so at the top. Show me the next run time before saving the routine.
```

When the Bot confirms, check the owning Bot, schedule and time zone, input sources, expected result (the draft report here, plus a draft to you only in the variant), approval boundary (nothing sent or shared) and what it does when a source is missing. Then press **Test run**. A test run does real work, so it will read your real email, calendar and tasks, and in the variant it will create a real draft.
