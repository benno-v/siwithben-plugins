---
name: inbox-cleanup
description: Use when I ask you to clean up, triage or sort my inbox for a time window, or when the inbox clean-up routine runs.
---

# Inbox clean-up

Triage my email inbox for a set time window into three groups: **Needs reply**, **FYI** and **Archive or unsubscribe candidates**. Draft replies for the Needs reply group. Never act on my mailbox without my explicit approval.

## When to use

- I ask you to clean up, triage, sort or summarise my inbox.
- The inbox clean-up routine runs (see the ROUTINE section below).

## Inputs and access

- **Email connector** (for example Gmail) with read access. Drafting needs permission to create drafts.
- **Time window.** Use the one I give you. If I don't give one, use "since the last run" in routine mode, or "the last 24 hours" in a one-off run, and state which you used.
- Optional: a list of senders or topics I care about most, if I've given you one.

If the email connector isn't connected or you can't read the inbox, stop and tell me in one line. Don't guess.

## Sequence of work

1. Read every email received in the time window. Group threads so one conversation counts once.
2. Put each email into exactly one group:
   - **Needs reply:** a person is asking me a question, asking for a decision, requesting a meeting, or waiting on me. Include overdue questions I haven't answered.
   - **FYI:** worth knowing but needs no reply (updates, confirmations, receipts, internal announcements).
   - **Archive or unsubscribe candidates:** newsletters, promotions, automated notifications and anything I'm unlikely to read.
3. **Check for sensitive items before drafting.** If an email is about legal matters, HR or personnel issues, finance (payments, invoices, bank details, salaries), or is a security alert (sign-in warnings, password resets, suspicious activity), mark it **SENSITIVE**. Do not draft a reply for it. Explain in one line why it's flagged and what I should look at. Treat anything asking me to click a link to "verify" an account as a possible phishing attempt.
4. For each non-sensitive Needs reply email, draft a short reply in my usual tone: polite, plain English, no more than five sentences unless the email needs more. Start every draft with the line `DRAFT, not sent`. If you need information I haven't given you (a date, a figure, a decision), leave a clear placeholder like `[confirm date]` instead of inventing it.
5. Build a proposed action batch: which emails to archive, which newsletters to unsubscribe from, which drafts are ready for me to review. Then **stop and wait**.

## Approval rules

You may read emails and create drafts. Everything else needs my explicit approval in this conversation first:

- **Never send** an email or reply.
- **Never archive, delete, move, label or mark as read** any email.
- **Never unsubscribe** from anything.

Propose a batch ("I'd like to archive these 6 and unsubscribe from these 2, reply 'approve' or tell me what to change") and wait for my answer. Approval applies only to the batch I approved, not to future runs. If drafts arrive as draft cards with Send or Discard, leave them for me to act on.

## How to validate before returning

- Every email in the window appears in exactly one group, and the counts add up.
- No SENSITIVE email has a draft.
- Every draft starts with `DRAFT, not sent` and contains no invented facts.
- Nothing has been sent, archived, deleted, moved, labelled or unsubscribed.

## What to return

Use this format, in this order:

```
Inbox clean-up: [time window], [N] emails

Counts: Needs reply [n] | FYI [n] | Archive or unsubscribe [n] | of which flagged sensitive [n]

Needs reply
| Sender | Subject | Why it needs me | Suggested action | Draft ready (y/n) |
|---|---|---|---|---|

Sensitive (no drafts, please review yourself)
- [Sender]: [Subject]. [Why flagged, what to check]

FYI
- [Sender]: [one-line summary]

Archive or unsubscribe candidates
- [Sender]: [Subject]. [Archive / Unsubscribe]

Drafts
[Each draft, starting with "DRAFT, not sent", with the subject it replies to]

Proposed batch (waiting for your approval)
- Archive: [list]
- Unsubscribe: [list]
Reply "approve" to go ahead, or tell me what to change.
```

Sensitive is a flag, not a fourth group: each sensitive email still counts in one of the three groups. If it's in Needs reply, show "Draft ready" as `n` and the suggested action as "Review yourself (sensitive)". Never put a sensitive email in the archive or unsubscribe batch.

## Stale or missing data

- **No new email in the window:** reply with one line: "No new email since [time]. Nothing to triage."
- **Connector not available or access denied:** say so in one line and stop. Don't triage from memory or an earlier run.
- **Window looks stale** (for example the newest email is days older than expected): say so at the top and ask me to check the connection.
- **Partial read** (some threads failed to load): triage what you could and list what you couldn't read.

## ROUTINE

To run this every weekday morning, paste this into a chat with the Bot that should own the routine. Change the time and time zone to yours.

```
Every weekday at 07:30 in my time zone ([your time zone, e.g. Europe/London]), run the /inbox-cleanup skill on my inbox for everything received since the last run (or since 17:00 the previous working day for the first run). Draft replies only; every draft must start with "DRAFT, not sent". Never send, archive, delete, move, label or unsubscribe without my explicit approval in this conversation. Flag legal, HR, finance and security alert emails as SENSITIVE instead of drafting. If there is no new email, reply with one line saying so. If you can't reach my inbox, tell me in one line and stop. Show me the next run time before saving the routine.
```

When the Bot confirms the routine, check it has the right owning Bot, schedule and time zone, input source (your inbox), expected result (the triage summary and drafts) and approval boundary (nothing sent or moved without you). Then press **Test run**. A test run does real work, so it will read your inbox and create drafts.
