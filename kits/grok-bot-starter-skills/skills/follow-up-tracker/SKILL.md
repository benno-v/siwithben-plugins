---
name: follow-up-tracker
description: Use when I ask what I'm waiting on, who I owe a reply, or what follow-ups are due, or when the daily follow-up routine runs.
---

# Follow-up tracker: never miss a follow-up

Each day, find the conversations that have gone quiet and the tasks about to fall due, list them briefly, and draft polite nudges for me to review. Never send anything.

## When to use

- I ask "what am I waiting on?", "who do I owe a reply?", "what's due?" or "check my follow-ups".
- The follow-up tracker routine runs (see the ROUTINE section below).

## Inputs and access

- **Email connector** (for example Gmail) with read access to Inbox and Sent. Drafting needs permission to create drafts.
- **Look-back window:** the number of days I give you. Default is **7 days**.
- **Task tool** (for example Notion or another connected task list), if connected. If not connected, skip that part and say "Task tool not connected" in one line.
- **Previous nudges:** earlier drafts, sent nudges and any notes from previous runs, so you don't nudge the same person too often.

If the email connector isn't available, stop and tell me in one line. Don't work from memory.

## Sequence of work

1. **Waiting on others.** Check emails I sent in the look-back window. Include a thread when my message asked a question or made a request and nobody has replied since. Ignore threads where the other person replied, where I only said thanks or confirmed something, and automated addresses (no-reply).
2. **Others waiting on me.** Check emails I received in the look-back window where someone asked me a question or for something, and I haven't replied since.
3. **Tasks due soon.** If a task tool is connected, list open tasks due today or in the next 2 days, plus any already overdue.
4. **Missing owner or date.** If a task or request has no clear owner, mark it **Owner missing**. If it has no clear due date, mark it **Due date missing**. Don't guess either one.
5. **Nudge cooldown.** Before drafting a nudge, check previous drafts, sent messages and notes. If I've already nudged that person (any thread) in the last **3 working days**, don't draft another. Mark the item "Nudged [date], cooling off".
6. **Draft nudges** for items in the Waiting on others group that pass the cooldown. Keep them short, warm and specific: remind them what I asked, when, and what I need. Start every draft with the line `DRAFT, not sent`. For items in the Others waiting on me group, draft a reply only if the answer is clear from the thread; otherwise suggest what I need to decide.

## Approval rules

- **Never send** a nudge, reply or any message. Create drafts only.
- Don't change, complete, reassign or re-date tasks in the task tool.
- Don't archive, label or move any email.
- If drafts arrive as draft cards with Send or Discard, leave them for me to act on.

Anything beyond reading and drafting needs my explicit approval in this conversation, for that specific item.

## How to validate before returning

- Each item appears once, in the right group.
- No item has an owner or due date you guessed. Gaps are marked "Owner missing" or "Due date missing".
- No nudge goes to someone already nudged in the last 3 working days.
- Every draft starts with `DRAFT, not sent`. Nothing has been sent.

## What to return

Keep it short. Use this format:

```
Follow-ups: last [N] days, checked [date and time]

Waiting on others ([n])
- [Person]: [what I asked], sent [date], [X] working days ago. [Nudge drafted / Nudged [date], cooling off]

Waiting on me ([n])
- [Person]: [what they asked], received [date]. [Reply drafted / Needs your decision: ...]

Due in the next 2 days ([n])
- [Task]: due [date], owner [name or "Owner missing"]
- [Task]: due ["Due date missing"], owner [name]

Drafts
[Each draft, starting with "DRAFT, not sent", with the subject it relates to]
```

Leave out any empty group.

## Stale or missing data

- **Nothing waiting:** in a one-off run, reply with one line: "Nothing waiting: no open follow-ups or tasks due in the next 2 days." In routine mode, stay silent (or post that one line only if I've asked for a daily confirmation).
- **Email connector not available:** say so in one line and stop.
- **Task tool not connected:** do the email checks and add "Task tool not connected" at the end.
- **Data looks stale** (for example nothing in Sent for several working days when I'm normally active): say so at the top and ask me to check the connection.

## ROUTINE

Suggested schedule: weekdays at 16:00, so there's time to act before the end of the day. Paste this into a chat with the Bot that should own the routine and change the time zone to yours.

```
Every weekday at 16:00 in my time zone ([your time zone, e.g. Africa/Johannesburg]), run the /follow-up-tracker skill with a 7-day look-back. Check sent emails with no reply, emails waiting on my reply, and tasks due in the next 2 days if my task tool is connected. Draft polite nudges only; every draft must start with "DRAFT, not sent". Never send anything. Don't nudge the same person twice within 3 working days. Mark items "Owner missing" or "Due date missing" rather than guessing. If nothing is waiting, stay silent. If you can't reach my email, tell me in one line. Show me the next run time before saving the routine.
```

When the Bot confirms, check the owning Bot, schedule and time zone, input sources (email and task tool), expected result, approval boundary (drafts only) and what it does when a source is missing. Then press **Test run**. A test run does real work, so it will create real drafts.
