# Routine templates

Routines are what make this a system rather than a chat: they run in the background on Grok's own computer, so I don't need my laptop open ([04:19 in the video](https://youtu.be/UBX3qXaFlgw?t=259)). My weekly rhythm is each bot doing a little task across the days of the week ([15:17](https://youtu.be/UBX3qXaFlgw?t=917)).

## How to read these templates

- **Schedule in plain English** is what you tell your bot. Grok Bot takes routine schedules in plain English (for example "Every Friday at 12:00 in my time zone"), so that's the part to paste.
- **Cron** is the same schedule in the compact five-field notation (minute, hour, day of month, month, day of week; Sunday is 0). It's there only to help you keep your weekly plan tidy; don't assume the app wants it. Check the schedule the bot confirms back.
- **Times are my suggestions, not my own schedule.** The video shows what runs on which day, not the exact times. Pick times that suit your week, and always include your time zone.
- Run each job once by hand first ([12-jobs.md](../prompts/12-jobs.md)). Press **Test** on a new routine; a test does real work, so use data you're happy for the bot to read.
- Routine schedules must be at least five minutes apart, and a Bot can own up to 50 routines. Deleting a routine has no undo, so pause it if you're unsure. The [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) cover the details.
- Each routine below ends with the approval boundary and a stale-data rule. Keep them. Check your [approval rules](../templates/approval-rules.md) match.

## Weekly rhythm (fill in your own)

| Day | Time | Routine | Owner |
|---|---|---|---|
| Every morning on training days | [time] | Daily session plan | Fitness coach |
| Monday to Friday | [time] | Inbox triage | Inbox bot |
| Monday to Friday | [time] | Meeting notes to actions | Primary bot |
| Every day | [time] | Morning summary | Primary bot |
| Every day | [time] | Shopper price check | Personal shopper |
| Friday | [time] | Grocery basket and email | Food bot |
| Saturday | [time] | Weekend summary | Primary bot |
| Sunday | [time] | Workout planning for next week | Fitness coach |
| Sunday | [time] | Budget check-in | Money bot |
| Monday | [time] | Content ideas | Research bot |

## The routines

Replace the bits in square brackets. Every routine says "show me the next run time before saving". Do that.

### R1. Daily session plan (job 3)

Owner: fitness coach. Suggested: training days at 06:30. Cron: `30 6 * * 1,3,5` (Mon, Wed, Fri; change to your days).

```
On my training days ([your days, e.g. Monday, Wednesday and Friday]) at [06:30] in my time zone ([your time zone]), send me today's training session from this week's plan in my [Notion] log: exercises, sets, reps and weights, short enough to read on my phone. If today isn't a training day or there is no plan for this week, say so in one line. Send it as a notification to me only. Don't add anything to my calendar or message anyone else. Show me the next run time before saving the routine.
```

### R2. Workout planning for next week (job 1)

Owner: fitness coach. Suggested: Sunday 18:00. Cron: `0 18 * * 0`.

```
Every Sunday at [18:00] in my time zone ([your time zone]), read the workouts I logged this week in [Notion] and set up next week's training plan: every exercise, with sets, reps and the weight to use. Raise weights only where my logs and effort ratings support it, and say why in one line. Save the plan in [Notion] and show it to me here. If my log has no entries this week, tell me and ask instead of guessing. Don't add anything to my calendar or message anyone. Show me the next run time before saving the routine.
```

### R3. Weekly grocery basket (job 4)

Owner: food bot. Suggested: Friday 12:00. Cron: `0 12 * * 5`.

```
Every Friday at [12:00] in my time zone ([your time zone]), build next week's grocery basket from the meal plan in [Notion] at [my online stores], within my weekly budget of [amount]. If I went over budget in the last weeks, tighten the list and tell me what you changed. Fill the basket using your own browser, then stop: never check out or pay. Email me the list, the total, the budget left, substitutions and anything out of stock, as a draft or message to me only. If the meal plan is missing, tell me in one line instead of guessing. Show me the next run time before saving the routine.
```

### R4. Budget check-in (job 5)

Owner: money bot. Suggested: Sunday 19:00. Cron: `0 19 * * 0`.

```
Every Sunday at [19:00] in my time zone ([your time zone]), run my budget check-in from [my budgeting app]: for each budget line show spent so far this month, my limit and what's left, and flag lines that are close to or over their limit. Propose next week's adjustment and wait for my yes before treating it as the plan. Add reminders for statements, subscriptions to review and receipts to file. Read and advise only: never connect a bank account, pay, transfer or cancel anything. If the data is missing or stale, say which period it covers, at the top. Save a short record in [Notion]. Show me the next run time before saving the routine.
```

### R5. Morning summary (job 6)

Owner: primary bot. Suggested: daily 07:00. Cron: `0 7 * * *`.

```
Every day at [07:00] in my time zone ([your time zone]), send me my morning summary: today's calendar, anything due or overdue, the training session if there is one, emails flagged as important, the weather for [my city] and anything waiting for my approval. One screen, most important item first. Don't add anything to my calendar or send anything to anyone. If a source can't be reached, say so in one line. Show me the next run time before saving the routine.
```

### R6. Weekend summary (job 6)

Owner: primary bot. Suggested: Saturday 08:00. Cron: `0 8 * * 6`.

```
Every Saturday at [08:00] in my time zone ([your time zone]), send me my weekend summary: the weather for [my city], my calendar for the weekend, and a proposed plan for the day that fits both, as a draft I can accept or change. Don't add anything to my calendar until I say yes. Show me the next run time before saving the routine.
```

### R7. Calendar and reminders check (job 7)

Owner: primary bot. Suggested: weekdays 17:00. Cron: `0 17 * * 1-5`.

```
Every weekday at [17:00] in my time zone ([your time zone]), check my calendar for tomorrow and the rest of the week. Tell me about clashes, back-to-back meetings with no break and anything I might be forgetting. Propose calendar entries or reminders, as a list, and wait for my yes before adding any: never add anything to my calendar without it. Reminders to me alone are fine to set. If there is nothing to flag, stay silent. Show me the next run time before saving the routine.
```

### R8. Inbox triage (job 8)

Owner: inbox bot. Suggested: weekdays 07:30. Cron: `30 7 * * 1-5`.

```
Every weekday at [07:30] in my time zone ([your time zone]), triage my inbox for everything received since the last run. Tag each thread as needs reply, FYI, or newsletter and spam candidate, flag what I might have missed, and write drafts for the ones that need a reply, each starting with "DRAFT, not sent". Flag legal, HR, money and security-alert emails as sensitive and don't draft replies to them. Propose a batch to archive or unsubscribe from and wait for my approval. Never send, archive, delete or unsubscribe on your own. If there is no new email, say so in one line. If you can't reach my inbox, tell me in one line and stop. Show me the next run time before saving the routine.
```

### R9. Meeting notes to actions (job 11)

Owner: primary bot. Suggested: weekdays 17:30. Cron: `30 17 * * 1-5`.

```
Every weekday at [17:30] in my time zone ([your time zone]), read the meeting notes I filed in [Notion] today. List the decisions and the action items with owner and due date; ideas and maybes go in a separate list. Never guess an owner or a date; flag what's missing. Propose reminders for my own actions and calendar entries for follow-up meetings, and wait for my yes before creating any. Don't message anyone. If there are no new notes, stay silent. Show me the next run time before saving the routine.
```

### R10. Content ideas (job 10)

Owner: research bot. Suggested: Monday 09:00. Cron: `0 9 * * 1`.

```
Every Monday at [09:00] in my time zone ([your time zone]), look at what people are interested in for [my topics] and add [5] content ideas to my list in [Notion], each marked "To review", with the evidence and sources. Don't change or delete my existing ideas, and don't publish or post anything. Tell me the strongest three in one short message. Show me the next run time before saving the routine.
```

### R11. Shopper price check (job 12)

Owner: personal shopper. Suggested: daily 09:00. Cron: `0 9 * * *`.

```
Every day at [09:00] in my time zone ([your time zone]), check the current price and stock of each item on my watch list in [Notion] at the stores listed there. Update the price history. Tell me only when something changed in a way I care about: a price drop, the lowest price so far or back in stock, with the item, price, store and link. Never buy or check out anything. If a page can't be read, tell me which one in one line instead of guessing a price. Show me the next run time before saving the routine.
```

## Research (job 9) and session logging (job 2)

These two don't need a routine. Research runs when I ask. Session logging is me sending a message after a workout. The [research prompt](../prompts/12-jobs.md#9-research) is low risk, so it can run without asking; the approval rules in the next file say what else does.
