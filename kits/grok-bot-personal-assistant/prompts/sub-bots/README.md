# Sub-bot prompts

One prompt per sub-bot. Each is the standing instruction for that bot: what it does, what it connects to, where it saves things, and what it must ask me about first.

## How to use them

1. Create the sub-bot in the Grok Bot app (I show my six at [00:26](https://youtu.be/UBX3qXaFlgw?t=26)).
2. Paste its prompt as the bot's first message, fill in the square brackets (or let it ask you), and say: **"Save this as your standing instructions."**
3. Run one job by hand before you schedule anything (see [12-jobs.md](../12-jobs.md)).
4. Keep your instructions going through the primary bot ([00-primary-bot-setup.md](../00-primary-bot-setup.md)).

| Sub-bot | File | Connects to |
|---|---|---|
| Fitness coach | [fitness-coach.md](fitness-coach.md) | Notion, calendar (optional) |
| Food bot | [food-bot.md](food-bot.md) | Notion, email, its own browser for shops |
| Money bot | [money-bot.md](money-bot.md) | Budgeting app (read only), Notion, calendar |
| Inbox bot | [inbox-bot.md](inbox-bot.md) | Gmail, Google Calendar |
| Research bot | [research-bot.md](research-bot.md) | Google Drive, Notion, its own browser |
| Personal shopper | [personal-shopper.md](personal-shopper.md) | Its own browser, Notion |

Every prompt ends with the same three rules: drafts first, a yes before anything is spent or sent, and no guessing. Your own [approval rules](../../templates/approval-rules.md) go on top of these.
