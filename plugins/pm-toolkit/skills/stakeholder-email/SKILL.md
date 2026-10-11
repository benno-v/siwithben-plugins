---
name: stakeholder-email
description: Draft a concise stakeholder email from this week's priorities and decisions — subject, short context, priorities, decisions needed with dates, and an ask. Never sends anything; can match an example of the user's tone if one is given. Use when the user asks to write, draft or send a stakeholder/client/sponsor update email.
---

# Stakeholder email

Draft a short, sendable stakeholder email from this week's priorities and decisions. This skill only drafts text — it never sends, schedules or posts anything.

## Ground rules

- Work only from what the user gives you (this week's priorities, decisions, status report, meeting notes) or what you can read in the connected folder. Never invent figures, dates, names or commitments.
- Where something is missing, write "Not provided" or "TBC" rather than guessing — especially dates for decisions.
- This skill drafts only. Never send, schedule, or submit the email through any channel; always hand back the draft as text for the user to send themselves.
- Keep it short: a stakeholder should be able to read it in under a minute. No jargon, no technical detail that doesn't matter to them.
- Plain business English.

## Inputs to look for

This week's priorities and decisions (from the `weekly-priorities` skill's output, a status report, meeting notes, or whatever the user pastes), who the email is to (name/role, so tone and detail level fit), and the sender's name if not obvious. Before asking, check the connected folder / current working directory for a recent status report or meeting notes to pull from. If anything is still missing after that, ask once, in one short numbered list.

Also ask (once, as part of that same list if needed): does the user have an example of their own tone to match (a previous email, or a style note)? If they provide one, mirror its tone, formality and typical sign-off; if not, default to a professional, warm, concise tone.

## Method

1. Pull 2–4 priorities/updates relevant to this specific stakeholder — not everything on the internal list, only what they need to know or act on.
2. Pull any decisions that need this stakeholder's input, each with what's being asked and a date if one exists. If no date is known, write "by: TBC" rather than inventing urgency.
3. End with exactly one clear ask — what you want the reader to do next (approve, reply, attend, review). If there's truly nothing needed from them, say "No action needed — for your information."
4. If a tone example was given, match its sentence length, greeting/sign-off style and formality; otherwise keep it professional and warm.

## Output format

```
**To:** <name/role or "Not provided"> **Subject:** <short, specific subject line>

<Greeting>,

<1-2 sentence context: what this email is about and why now.>

**This week:**
- ...

**Decisions needed:**
- <decision> — by: <date or TBC>

<One clear ask, as a sentence, or "No action needed — for your information.">

<Sign-off matching the given tone, or a simple professional sign-off>
```

## Before handing over

Add one line: "This is a draft only — I haven't sent anything. Check names, dates and the ask, then send it yourself."
