# Sample idea to red-team (fictional)

Test input for `skills/red-team-review`. Northwind Traders is a fictional company. Paste everything below the line into a chat and say: "Run /red-team-review on this."

**What to check in the output:** a two-line steelman, severity tags on every point, likelihood and impact on every risk, no invented statistics, a verdict, a top 3 fixes list, and no rewritten version of the proposal.

---

## Proposal: replace weekly status meetings with an AI-written async report

**From:** Operations PMO, Northwind Traders
**Decision needed by:** four weeks from today

### The problem

Every Monday, 14 people spend an hour in the operations status meeting. Most of the time goes on each team lead reading out updates that are already in our project tracker. Decisions often get pushed to "next week" because the right people aren't in the room, and people working on the late shift can't attend.

### The idea

Cancel the weekly status meeting. Instead, every Monday at 08:00 an AI assistant reads the project tracker, the team channels and last week's notes, then writes a one-page status report with a RAG rating per workstream, key risks and decisions needed. The report goes out to everyone by email at 09:00. Anyone with a question replies in the thread.

### Why it's worth it

- Saves 14 hours of meeting time a week, roughly 700 hours a year.
- Late-shift staff get the same information as everyone else.
- Reports follow the same format every week, so trends are easier to spot.
- Team leads stop spending Sunday evening preparing slides.

### How we'd roll it out

1. Switch it on for all workstreams from the Monday after the decision.
2. Cancel the Monday meeting the same week.
3. The PMO checks the first report; after that it runs automatically.

### Costs

- AI assistant licences for the PMO (already budgeted).
- About two days of PMO time to set it up.

### What we haven't decided yet

- Who signs off the RAG ratings.
- What happens when the tracker hasn't been updated.
- Where decisions get made if there's no meeting.
