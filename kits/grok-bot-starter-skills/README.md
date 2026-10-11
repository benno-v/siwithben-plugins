# Grok Bot starter skills by SI with Ben

![Grok Bot Starter Skills by SI with Ben](preview.png)

**Download:** [grok-bot-starter-skills.zip](../grok-bot-starter-skills.zip) has everything in this folder (four skills, the two-jobs example and sample test data).

I put this kit together so you can set up the Grok Bot examples from my video in about fifteen minutes. You get four ready-to-save skills: one that cleans up your inbox, one that makes sure you never miss a follow-up, one that red-teams your ideas before you commit to them, and one that drafts your weekly project status report. Each skill drafts and proposes; you stay in control of anything that gets sent, moved or deleted.

*By Benjamin Vermeulen, SI with Ben ([@SIwithBen](https://www.youtube.com/@SIwithBen)).*

## What's new in 1.1.0

- New `weekly-status-report` skill: the status report that writes itself at the end of every week, which I tease in the video at [14:56](https://youtu.be/O5bHcw_EHQs?t=896). It gathers the week's email, calendar, tasks and meeting notes, drafts a Green, Amber or Red report in a fixed format, and never sends it. Sample data dates are now relative ("Yesterday 16:45", "This Wednesday"), so the tests never look stale.

## The video

[Practical Grok Bot Examples](https://youtu.be/O5bHcw_EHQs). Jump straight to each part:

| Part | Timestamp |
|---|---|
| Inbox clean-up | [02:42](https://youtu.be/O5bHcw_EHQs?t=162) |
| Inbox clean-up results | [13:24](https://youtu.be/O5bHcw_EHQs?t=804) |
| Follow-ups | [04:55](https://youtu.be/O5bHcw_EHQs?t=295) |
| Two jobs at once | [05:14](https://youtu.be/O5bHcw_EHQs?t=314) |
| Staying in control | [05:59](https://youtu.be/O5bHcw_EHQs?t=359) |
| Red team | [07:20](https://youtu.be/O5bHcw_EHQs?t=440) |
| Weekly status report (teaser) | [14:56](https://youtu.be/O5bHcw_EHQs?t=896) |

## What's in the kit

| File | What it's for |
|---|---|
| `skills/inbox-cleanup/SKILL.md` | Sorts your inbox into Needs reply, FYI and Archive or unsubscribe candidates, drafts replies, flags sensitive emails. Includes a paste-ready routine. |
| `skills/follow-up-tracker/SKILL.md` | Daily check of who you're waiting on, who's waiting on you and what's due in the next 2 days. Drafts polite nudges. Includes a paste-ready routine. |
| `skills/red-team-review/SKILL.md` | A tough but fair review of an idea, plan, build or document, with a verdict and top 3 fixes. Never edits your work. |
| `skills/weekly-status-report/SKILL.md` | Gathers the week's email, calendar, tasks and meeting notes for a project and drafts a one-page status report with a Green, Amber or Red rating, sources and missing data. Never sends it. Includes a paste-ready routine. |
| `examples/two-jobs-at-once.md` | A paste-ready prompt for running background research while your Bot drafts a meeting agenda with you. |
| `tests/sample-data/` | Fictional inbox, sent emails, tasks, an idea and a week of project evidence, so you can try the skills without touching real data. Dates are relative ("Yesterday", "This Wednesday"), so they never look stale. |

Each skill follows the same pattern: when to use it, what access it needs, the sequence of work, how to check the result, what to return, and what needs your approval.

## Requirements

- **Grok Bot access.** See [x.ai/bot](https://x.ai/bot) for current availability.
- **Connectors, only the ones you need:**
  - Inbox clean-up: your email (for example Gmail).
  - Follow-up tracker: your email, plus a task tool (for example Notion) if you want tasks included.
  - Two jobs at once: your calendar, plus a task tool if you want tasks in the agenda.
  - Red team review: nothing. Paste the work into the chat.
  - Weekly status report: whichever of these you use for the project: email, calendar, a task tool (for example Notion) and wherever you keep meeting notes. It works with fewer sources and lists what's missing.

## Setup

### 1. Add each skill

1. Open a chat with your Bot.
2. Paste the full contents of a `SKILL.md` file and say: **"Save this as a private skill called inbox-cleanup."** (Use `follow-up-tracker`, `red-team-review` or `weekly-status-report` for the others.)
3. Type `/` in the desktop composer and check the skill appears in the menu. Private skills are one library shared by all your Bots, so you only add each one once.
4. If it isn't in the `/` menu, go to **Marketplace > Your plugins > Manage plugins and skills > Private skills** and check it's there.

Quick reminder: `/` is for skills, `@` is for Bots, groups, routines and connectors.

### 2. Test with a one-off run first

Before you schedule anything, run each skill once by hand. For example: "Run /inbox-cleanup on my inbox for the last 24 hours." Check the output format, that drafts are labelled "DRAFT, not sent", and that nothing was sent or moved.

To try it with no real data at all, paste a file from `tests/sample-data/` into the chat and ask the Bot to run the skill on that text instead.

### 3. Create the routine

1. Open a chat with the Bot that should own the routine.
2. Paste the prompt from the **ROUTINE** section at the bottom of the skill (inbox clean-up suggests weekdays at 07:30, follow-up tracker suggests weekdays at 16:00, weekly status report suggests Fridays at 14:00). Change the time zone to yours.
3. Before you accept, confirm the owning Bot, the schedule and time zone, the input source, the expected result, the approval boundary, and what happens when a source is missing.
4. The Bot shows the next run time. Background routines run even with your laptop closed.
5. Press **Test run**. A test run does real work, so it will read real email and create real drafts.

### The weekly status report routine

I run this on Fridays at 14:00, which leaves me time to review the draft before the end of the week. Paste this into a chat with the Bot that should own it and change the bits in square brackets:

```
Every Friday at 14:00 (my time zone: [your time zone, e.g. Europe/London]), run the /weekly-status-report skill for [project name]. Use evidence from Monday 00:00 to now in my time zone, from these sources: my email (sent and received), my calendar, [my Notion project tracker or other task tool] and meeting notes in [where you keep them]. Write the report in the skill's fixed format, labelled "DRAFT, not sent", with an overall Green, Amber or Red status, a Sources list and a Missing data list. Write "Not provided" for anything you can't find; never invent owners, dates, milestones, budget figures or percentages, and never fill a gap with data from before this week. Return the report here in this conversation only. Never send, post or share it, and don't create drafts to anyone. If a source is unavailable or has nothing from this week, say so at the top. Show me the next run time before saving the routine.
```

If you'd like the draft waiting in your mailbox too, use the "send to me only" variant at the bottom of `skills/weekly-status-report/SKILL.md`. It creates one email draft addressed to you alone, with the subject "DRAFT status report: [project], week ending [date]", and still never sends anything to stakeholders. The same warning applies: **Test run** does real work, so it reads your real email, calendar and tasks.

### 4. Check the Routines panel

Open the Bot, then **View conversation details > Routines**. From there you can pause, test, edit, view history or delete a routine. Deleting has no undo, so pause instead if you're unsure.

Limits worth knowing: up to 50 routines per Bot, and schedules need to be at least five minutes apart.

## Staying in control

These are the rules I follow, and the skills are written to match them:

- **Leave drafts ON.** Email and Slack messages arrive as editable draft cards with Send or Discard. There's a per-Bot "Disable drafts" option; please don't use it with these skills.
- **Approve every send.** Nothing goes out, gets archived, deleted, moved or unsubscribed unless you say so in the conversation.
- **Read-only first.** Start with read access and drafts. Widen access only once you trust the results.
- **Connect only what you need.** Each skill lists what it needs. Don't connect extra tools "just in case".
- **Reports stay drafts.** The weekly status report comes back to you in the chat. At most it saves a draft addressed to you; you decide who sees it.
- **Check sensitive items yourself.** The inbox skill flags legal, HR, finance and security alert emails instead of drafting replies. Those are yours to handle.

## Featured in

- Video: [Practical Grok Bot Examples](https://youtu.be/O5bHcw_EHQs)
- Grok Bot docs: [Skills, routines and automations](https://docs.x.ai/grok-bot/skills-routines-and-automations)
- Channel: [youtube.com/@SIwithBen](https://www.youtube.com/@SIwithBen)

## Licence

MIT. See [LICENSE](LICENSE). Use it, adapt it, share it with your team.
