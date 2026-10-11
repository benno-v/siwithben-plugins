**Red team review: Replace weekly status meetings with an AI-written async report (Northwind Traders, Operations PMO)**

**Steelman**
Most of the meeting is people reading out updates already in the tracker. A consistent written report that everyone can read, including late-shift staff, would recover a lot of time and make trends easier to see.

**Assumptions**
- **[Critical]** *The tracker and team channels are accurate and current enough for the AI to summarise.* The proposal itself lists "what happens when the tracker hasn't been updated" as undecided. If the inputs are stale, the report will look authoritative but be wrong.
- **[Critical]** *The status meeting is mainly for sharing information.* The problem statement also says decisions get pushed to "next week." The proposal takes away the only regular decision forum and puts nothing in its place ("Where decisions get made if there's no meeting" is undecided).
- **[Major]** *An AI can assign reliable RAG ratings per workstream.* A RAG rating is a judgement call, and the proposal doesn't say who signs it off. An unchecked Green on a workstream that is really Amber is the most costly kind of error here.
- **[Major]** *People will read a 09:00 email and raise questions in the thread.* Replacing a meeting people must attend with an email people can ignore depends on behaviour that hasn't been tested.
- **[Minor]** *Team leads currently spend Sunday evenings building slides.* The problem statement says the updates are "already in our project tracker." If so, it's unclear what the slides contain. If leads were adding context the tracker lacks, the AI won't have that context.

**Failure modes**
- **[Critical]** The tracker isn't updated, so the AI produces a confident report from old data. Leaders act on it, and no one notices until a workstream slips.
- **[Critical]** Decisions that used to stall now don't get made at all. Email threads spread out, the "right people" are still missing, and items quietly age.
- **[Major]** After the first week, nobody reviews the report. Errors or hallucinated risks then build up and trust in the report falls. Once trust is gone, people quietly bring back side meetings, which wipes out the time saving.
- **[Major]** Reading team channels could pick up sensitive or informal content, such as HR matters, frank opinions, or customer details, and repeat it in a report sent to everyone.
- **[Minor]** Reply-all threads on a 14-person email turn into a slower, messier meeting.

**Risks**

| Risk | Likelihood | Impact | Severity |
|---|---|---|---|
| Stale tracker data leads to an inaccurate report | High | High | Critical |
| No forum for making decisions, so decisions are delayed | High | High | Critical |
| Wrong RAG rating with no human sign-off | Med | High | Major |
| Low readership or engagement with the email | Med | Med | Major |
| Sensitive channel content appears in the report | Med | High | Major |
| Hard cutover with no fallback causes disruption | Med | Med | Major |
| Licence or access scope doesn't cover all channels (unverified) | Low | Med | Minor |

**Missing evidence**
- **[Major]** How current the tracker really is today, for example how often items are updated before Monday. This is the main thing the plan depends on.
- **[Major]** How many decisions the current meeting actually makes or defers, and who needs to be present for them.
- **[Major]** Whether the AI assistant is allowed to read team channels under internal data and privacy policy, and whether staff have been told.
- **[Minor]** The "roughly 700 hours a year" figure counts only meeting time. It doesn't subtract time spent reading the report, replying in threads, PMO review, or fixing tracker data. The net saving is unverified.
- **[Minor]** Whether the AI licences already budgeted "for the PMO" cover the access this needs. This is unverified.

**Cheapest test to de-risk**
- For 3 to 4 weeks, generate the AI report each Monday but keep the meeting, shortened to cover only decisions and exceptions. Each week, team leads mark any wrong RAG ratings or facts in the report.
- What would change my mind: if leads correct almost nothing and the shortened meeting clears decisions quickly, cancelling is justified. If corrections are frequent or caused by stale tracker data, fix the inputs before cutting the meeting.

**Who would object and why**
- **Team leads:** They'll be judged on an AI's RAG rating of their workstream without a chance to give context.
- **Senior stakeholders and decision makers:** They lose a predictable slot to make calls and to question people directly.
- **Late-shift staff:** They may welcome the change, but replying in an email thread isn't the same as having a voice in decisions.
- **IT, security or data protection:** An AI reading team channels and sending summaries to everyone raises access and confidentiality questions.
- **PMO:** "Runs automatically after the first check" leaves them responsible for accuracy without the time to ensure it.

**Verdict: Proceed with changes**
The information-sharing half of the idea is sound. However, the three "haven't decided yet" items aren't details: two of them, stale data and where decisions get made, are Critical gaps. The plan shouldn't start on 2 November until they're settled.

**Top 3 fixes**
1. Set up a decision forum before cancelling anything. That could be a short, decisions-only meeting or a named owner and deadline for each decision.
2. Name a human owner who signs off RAG ratings each week. Add a rule for what the report does when tracker data is stale, for example flagging the item rather than rating it.
3. Replace the hard cutover with a parallel-run pilot that has clear success criteria. Also get data and privacy sign-off before the AI reads team channels.

Status: Review only. I haven't edited the proposal, and nothing has been sent, archived or drafted. If you'd like to share this review, I can draft it for you to approve.
