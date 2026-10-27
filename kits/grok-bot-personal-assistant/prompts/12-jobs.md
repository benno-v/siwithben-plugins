# The 12 jobs

These are the 12 jobs in my setup, in the order I list them in the video ([07:46](https://youtu.be/UBX3qXaFlgw?t=466)). Each one is a prompt you can paste into your primary bot or into the sub-bot that owns it. Run each one once by hand first, check the result, and only then turn it into a routine with the [routine templates](../routines/routine-templates.md).

Change the bits in square brackets, or leave them and let the bot ask. Where a job writes to your notes app, I say Notion because that's what I use; use whatever you've connected.

Every job follows your [approval rules](../templates/approval-rules.md). Where a job could send, spend or change something, the prompt says so.

| # | Job | Owner | In the video |
|---|---|---|---|
| 1 | [Workout planning](#1-workout-planning) | Fitness coach | [07:52](https://youtu.be/UBX3qXaFlgw?t=472), [09:55](https://youtu.be/UBX3qXaFlgw?t=595) |
| 2 | [Session logging](#2-session-logging) | Fitness coach | [07:57](https://youtu.be/UBX3qXaFlgw?t=477), [10:18](https://youtu.be/UBX3qXaFlgw?t=618) |
| 3 | [Daily session plan](#3-daily-session-plan) | Fitness coach | [08:01](https://youtu.be/UBX3qXaFlgw?t=481), [10:36](https://youtu.be/UBX3qXaFlgw?t=636) |
| 4 | [Weekly grocery basket](#4-weekly-grocery-basket) | Food bot | [08:05](https://youtu.be/UBX3qXaFlgw?t=485), [10:47](https://youtu.be/UBX3qXaFlgw?t=647) |
| 5 | [Budget check-in](#5-budget-check-in) | Money bot | [08:10](https://youtu.be/UBX3qXaFlgw?t=490), [11:16](https://youtu.be/UBX3qXaFlgw?t=676) |
| 6 | [Morning and weekend summaries](#6-morning-and-weekend-summaries) | Primary bot | [08:21](https://youtu.be/UBX3qXaFlgw?t=501), [11:50](https://youtu.be/UBX3qXaFlgw?t=710) |
| 7 | [Calendar and reminders](#7-calendar-and-reminders) | Primary bot | [08:30](https://youtu.be/UBX3qXaFlgw?t=510), [12:18](https://youtu.be/UBX3qXaFlgw?t=738) |
| 8 | [Inbox triage and draft replies](#8-inbox-triage-and-draft-replies) | Inbox bot | [08:45](https://youtu.be/UBX3qXaFlgw?t=525), [12:37](https://youtu.be/UBX3qXaFlgw?t=757) |
| 9 | [Research](#9-research) | Research bot | [08:54](https://youtu.be/UBX3qXaFlgw?t=534), [12:54](https://youtu.be/UBX3qXaFlgw?t=774) |
| 10 | [Content ideas and trends](#10-content-ideas-and-trends) | Research bot | [09:11](https://youtu.be/UBX3qXaFlgw?t=551), [13:37](https://youtu.be/UBX3qXaFlgw?t=817) |
| 11 | [Meeting notes to actions](#11-meeting-notes-to-actions) | Primary bot | [09:21](https://youtu.be/UBX3qXaFlgw?t=561), [13:57](https://youtu.be/UBX3qXaFlgw?t=837) |
| 12 | [Personal shopper](#12-personal-shopper) | Shopper | [09:36](https://youtu.be/UBX3qXaFlgw?t=576), [14:15](https://youtu.be/UBX3qXaFlgw?t=855) |

## 1. Workout planning

Owner: fitness coach. Reads my logged workouts and sets up next week's plan.

```
Check my workout log in [Notion] for the sessions I logged this past week. Plan next week's training: for each training day list the exercises, sets, reps and the weight to use. Raise a weight only where my logs and effort ratings support it; hold or lower it where I skipped sessions or rated them very hard, and say why in one line. If the log is empty or older than two weeks, tell me and ask instead of guessing. Save the plan in [Notion] and show it to me here. Don't add anything to my calendar or message anyone.
```

## 2. Session logging

Owner: fitness coach. I message what I did; it logs it.

```
I'm logging a session. Date: [today]. Exercises, sets and weights: [e.g. bench press, 3 sets of 8 at 40 kg]. How hard it felt: [easy, ok or hard]. Save it to my workout log in [Notion] and read back exactly what you saved. If anything is missing or unclear, ask me before you save. Never fill in a number I didn't give you.
```

## 3. Daily session plan

Owner: fitness coach. A notification with the day's exercises.

```
Send me today's training session: the exercises, sets, reps and weights from this week's plan in [Notion]. If today isn't a training day, say so in one line. If there's no plan for this week, tell me and offer to build one. Keep it short enough to read on my phone before I leave.
```

## 4. Weekly grocery basket

Owner: food bot. Builds the basket from my meal plan, within budget.

```
Build next week's grocery basket from the meals in my plan: [my meal plan, or say "suggest meals first"]. List every item and quantity, minus what I already have: [items I have]. Work out the cost at [my online stores] and choose the combination that fits my budget of [amount] for the week. If I went over budget recently ([say so or "check my last check-ins"]), tighten the list and tell me what you changed. Fill the basket using your own browser, then stop: don't check out and don't pay. Email me the list, the total, the budget left, any substitutions and anything out of stock.
```

## 5. Budget check-in

Owner: money bot. Reads spending, flags risk, proposes next week's adjustment. Never moves money.

```
Do my budget check-in. Use my spending data from [my budgeting app, or the summary I paste below]. For each budget line, show spent so far this month, my limit and what's left. Flag every line that is close to or over its limit. Propose how to adjust next week's budget and wait for my yes before treating the new figures as the plan. Add reminders for anything I need to watch: statements, subscriptions to review, receipts to file. If the data is missing or stale, say which period it covers, at the top. Save a short record in [Notion]. Don't connect to a bank account, and don't pay, transfer or cancel anything.
```

## 6. Morning and weekend summaries

Owner: primary bot. My daily planner.

```
Give me my [morning / weekend] summary. Include: today's calendar, anything due or overdue, the training session if there is one, emails flagged as important by my inbox bot, the weather for [my city], and anything waiting for my approval. For a weekend summary, also propose a plan for the day that fits the weather and my calendar, as a draft I can accept or change. Don't add anything to my calendar until I say yes. Keep it to one screen, with the most important item first. If a source can't be reached, tell me in one line rather than leaving it out silently.
```

## 7. Calendar and reminders

Owner: primary bot, with the inbox bot feeding it.

```
Check my calendar for [the next 7 days]. Tell me what I might be forgetting: clashes, back-to-back meetings with no break, appointments with no travel time and anything with no agenda. Propose calendar entries or reminders for anything that needs one, as a list, and wait for my yes before adding any. If I ask you to move or cancel an appointment, draft the email to the other person, show it to me, and only after I approve it send it and update my calendar once they confirm.
```

## 8. Inbox triage and draft replies

Owner: inbox bot. See also the `inbox-cleanup` skill in the [starter skills kit](../../grok-bot-starter-skills).

```
Triage my inbox for [the last 24 hours]. Tag each thread as needs reply, FYI, or newsletter and spam candidate. Flag what I might have missed or what is coming up. Draft replies for the threads that need one, in my usual tone, each starting with "DRAFT, not sent", with placeholders such as [confirm date] where you need a fact from me, and a placeholder like [Yes, that works / No, I can't] where the answer is my decision. Never accept or decline anything for me. Flag legal, HR, money and security-alert emails as sensitive and don't draft replies to them. Propose a batch of emails to archive and senders to unsubscribe from, and wait for my approval. Don't send, archive, delete or unsubscribe anything on your own. If you can't reach my inbox, tell me in one line and stop.
```

## 9. Research

Owner: research bot. Low risk, so it can run without asking.

```
Research [topic or question]. Give me the key points, each with its source and the date of the source. Say what you couldn't verify and where sources disagree. For a purchase or trip, include options, prices, availability and, for a trip, the weather and where to stay. If I ask for a document, save it in [Google Drive] and tell me where it is. Don't send or publish anything.
```

## 10. Content ideas and trends

Owner: research bot. Adds ideas to a list I review.

```
Look at what people are interested in right now for [my topics]. Add [5] content ideas to my content ideas list in [Notion]. For each, give a working title, who it is for, the evidence for the interest (with sources) and how it fits what I already make. Mark each as "To review". Don't delete or change my existing ideas, and don't publish or post anything. Tell me the three you think are strongest and why.
```

## 11. Meeting notes to actions

Owner: primary bot. Works from the meeting notes I file in Notion.

```
Read the meeting notes I filed in [Notion] since [the last run]. For each meeting list the decisions and the action items, with owner and due date. Only list real commitments; ideas and maybes go in a separate list. Never guess an owner or a date: flag what is missing. Propose reminders for my own actions and calendar entries for any follow-up meetings, and wait for my yes before creating any. Don't message anyone. For a stricter version of this job, use the `notes-to-tasks` skill in the [starter skills kit](../../grok-bot-starter-skills).
```

## 12. Personal shopper

Owner: personal shopper. Finds, compares, watches, then asks.

```
Find me [product] with these must-haves: [must-haves] and a price limit of [amount]. Search [my stores]. Give me a table of the best options with price, store, stock, delivery time and link, and mark the lowest price. Add it to my watch list in [Notion] and check the prices [daily] from now on; tell me when the price drops, when it's at its lowest so far or when it's back in stock. When I say I want it, send me a ready-to-buy summary: exact item, price, store, delivery and link. Don't buy or check out anything unless I say yes to that exact item and price.
```
