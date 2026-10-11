---
name: project-summary
description: Read the project documents in the connected folder (proposal, SOW, contract, charter, risk register, status reports, meeting notes, change requests) and summarise where the project actually stands, with a source file for every fact. Use when the user asks "where are we on this project", wants a project summary or catch-up, or connects a project folder and asks what's in it.
---

# Project summary

Read everything available in the connected project folder and give a straight answer to "where are we?" — with a source file next to every fact, so the user can check it.

## Ground rules

- Work only from what you can actually read in the folder or what the user gives you. Never invent figures, dates, names, budgets or percentages. Where something is missing, write "Not provided" or "TBC".
- Every fact in the summary must carry its source file (e.g. "status-report-week8.md"). If you cannot find a source for something, do not include it.
- If documents conflict (e.g. two different budget figures), report both and say which file each came from; do not silently pick one.
- If key documents seem to be missing (no risk register, no recent status report), say so rather than leaving a silent gap.
- If the folder is empty, inaccessible, or nothing project-related is found, say so and ask the user to connect or point to the right folder. Do not guess.
- Plain business English, short bullets, no jargon.

## Inputs to look for

Look through the connected folder for anything project-related: proposal, SOW/contract, charter, risk register, status reports, meeting notes, change requests, budget trackers. Prioritise the most recent status report and meeting notes for current state; use the charter/SOW/contract for scope, budget baseline and timeline baseline.

If the folder has no date-stamped files to tell what's "latest", ask once which file is the most recent status update, then continue.

## Method

1. Skim every project document you can read; note its type and date (from filename or content).
2. Work out the current phase from the charter/SOW's plan versus what status reports/meeting notes describe as done or in progress.
3. For budget status: only calculate % spent vs % timeline elapsed if the documents actually give spend-to-date and a budget figure, and a start/end date or % complete. If any of those is missing, write "Budget status: not enough information in the documents provided" rather than estimating.
4. Pull open risks from the risk register (or from status reports/meeting notes if there is no register), highest score or most recently raised first.
5. Pull upcoming decisions from meeting notes, change requests and status reports — anything explicitly awaiting a decision, approval or sign-off.
6. Note things to watch: anything flagged as a concern, trend, or dependency, that is not yet a formal risk.

## Output format

```
# Project summary: <Project name or "Not provided">
As of: <date of most recent document used> · Sources reviewed: <list of filenames>

## Current phase
<1-3 sentences> — Source: <file>

## Budget status
<% spent vs % timeline elapsed, or "not enough information in the documents provided"> — Source: <file(s)>

## Open risks
- <risk> (<rating if given>) — Source: <file>

## Upcoming decisions
- <decision needed, who from, by when if given> — Source: <file>

## Things to watch
- <item> — Source: <file>

## Gaps noticed
- <missing document types, conflicting figures, or anything you could not verify>
```

## Before handing over

Add one line: "This summary only reflects what's in the connected folder. Check it against anything newer that hasn't been filed yet before you act on it."
