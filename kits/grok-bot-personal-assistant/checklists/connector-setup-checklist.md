# Connector setup checklist

The connectors I use are Gmail, Google Calendar, Google Drive and Notion, plus Grok's own computer and browser for routines ([03:09](https://youtu.be/UBX3qXaFlgw?t=189) and [05:29](https://youtu.be/UBX3qXaFlgw?t=329) in the video). Connect only what you need, one at a time, and test each before you add the next. Tick the boxes as you go.

I haven't listed screen-by-screen steps, because the apps change. Use Connect apps in the Grok Bot sidebar to find and install each app, and follow what the app asks. The [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) cover current steps.

## 0. Before you connect anything

- [ ] I have access to Grok Bot. In the video, access comes through the unified X subscription (Premium, Super or Ultra) ([00:13](https://youtu.be/UBX3qXaFlgw?t=13)). Check current availability at [x.ai/bot](https://x.ai/bot).
- [ ] I've filled in my [approval rules](../templates/approval-rules.md).
- [ ] I know which accounts I will not connect (for example bank accounts).
- [ ] I'm using the app on my phone for chat and notifications, and I've turned notifications on for the bots I want to hear from.

## 1. Gmail

What it's for: the inbox bot reads and tags mail and writes drafts; it sends only after I review and say yes ([05:19](https://youtu.be/UBX3qXaFlgw?t=319)). The food bot emails me the weekly basket summary.

- [ ] Connected the Gmail account I want the inbox bot to work on.
- [ ] Draft cards are ON (don't use the "disable drafts" option).
- [ ] Test 1 (read only): "List my last 5 emails and tell me which need a reply. Don't draft or send anything." Result matches my inbox.
- [ ] Test 2 (draft): "Draft a reply to [a test email] starting with DRAFT, not sent." A draft appears and nothing is sent.
- [ ] Test 3 (limits): "Reply to everyone and archive the rest." The bot refuses and proposes a batch instead.

## 2. Google Calendar

What it's for: seeing my calendar, proposing entries and, with my approval, adding them ([05:35](https://youtu.be/UBX3qXaFlgw?t=335)).

- [ ] Connected the calendar I want the bot to read.
- [ ] Test 1 (read only): "What's on my calendar tomorrow?" Result matches.
- [ ] Test 2 (propose): "Propose a 30-minute focus block tomorrow; don't add it yet." The bot proposes and waits.
- [ ] Test 3 (write, approved): "Yes, add it." The entry appears. Delete it afterwards.
- [ ] My level for adding or moving entries in the approval rules is set (suggested: needs my yes).

## 3. Google Drive

What it's for: letting the bot read my documents and save documents it writes, such as research I want to review ([05:40](https://youtu.be/UBX3qXaFlgw?t=340)).

- [ ] Connected Google Drive.
- [ ] Created a folder for the bots, e.g. "Assistant outputs", so their documents don't mix with mine.
- [ ] Test: "Research [a harmless topic] in five bullet points with sources and save it as a document in [folder]." The document is where the bot said.
- [ ] The bot tells me where every document is.

## 4. Notion (or your notes and database app)

What it's for: the central database the bots work from and post to, and where I can check and edit things by hand. The fitness coach, food bot and money bot save their records there, and my meeting notes and content ideas live there too ([05:50](https://youtu.be/UBX3qXaFlgw?t=350) and [06:11](https://youtu.be/UBX3qXaFlgw?t=371)).

- [ ] Connected Notion.
- [ ] Created the databases I need (see the list below) and shared only those with the bot.
- [ ] Test: "Add one test row to [database]." The row appears with the columns I expect. Delete it afterwards.
- [ ] Test: "Read the last two rows of [database] back to me." Correct.

Databases to create (names and columns are mine to suggest; change them to suit):

| Database | Used by | Suggested columns |
|---|---|---|
| Workout log | Fitness coach | Date, Exercise, Sets, Reps, Weight, Effort, Notes |
| Meal and grocery plans | Food bot | Week, Meals, Items, Estimated cost, Budget, Notes |
| Budget check-ins | Money bot | Date, Budget line, Spent, Limit, Flag, Notes |
| Content ideas | Research bot | Idea, Audience, Evidence, Source, Status |
| Meeting notes | Primary bot | Date, Meeting, Decisions, Actions, Owner, Due |
| Watch list | Personal shopper | Item, Store, Price, Lowest so far, Link, Last checked |
| Tasks | Primary bot | Task, Owner, Due, Status, Source |

For the Tasks database you can start from my [notion-action-list](../../notion-action-list) kit.

## 5. Budgeting app (optional)

What it's for: giving the money bot spending data without connecting bank accounts to the bot ([01:11](https://youtu.be/UBX3qXaFlgw?t=71) in the video, where I explain why I do it this way).

- [ ] I've decided whether to connect one. If not, I'll paste a spending summary into the chat for each check-in.
- [ ] If I connect one: read-only access, and no bank logins typed into the chat.
- [ ] Test: "Show my spending by category this month. Don't change anything." Totals match the app.

## 6. Grok's own computer and browser

What it's for: running routines on a schedule on Grok's computer, even with my laptop closed, and letting the shopper and food bot open stores and compare ([03:18](https://youtu.be/UBX3qXaFlgw?t=198) and [07:11](https://youtu.be/UBX3qXaFlgw?t=431)). It isn't a connector, but it's central.

- [ ] I've read what the bot can access on its computer and I'm happy with it.
- [ ] If a site needs a login, I give the bot access only through the app's secure sign-in. I never paste passwords into the chat.
- [ ] Test (browse): "Open [a shop I use] and find [a cheap item]. Tell me the price and link. Don't add it to a basket." Correct.
- [ ] Test (basket): "Add [a cheap item] to the basket and stop. Don't check out." The basket has the item and nothing is bought.

## 7. Routines

- [ ] Made one routine from the [routine templates](../routines/routine-templates.md) and checked the owning bot, schedule, time zone, source, result, approval boundary and what happens when a source is missing.
- [ ] Pressed **Test** and checked the result.
- [ ] Added the others one at a time, over a week or two, not all at once.

## 8. Review monthly

- [ ] Remove connectors I don't use.
- [ ] Re-read the approval rules.
- [ ] Check what the routines did and whether they still make sense.
