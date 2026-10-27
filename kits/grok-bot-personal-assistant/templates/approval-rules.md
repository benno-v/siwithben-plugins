# Approval rules template

In the video I define the rules for Grok myself: where I only want a draft, where I need to approve, and what can run on its own. Summaries and research don't need my approval ([15:30](https://youtu.be/UBX3qXaFlgw?t=930)). Drafts come to me first, and email is sent only after I review it ([04:57](https://youtu.be/UBX3qXaFlgw?t=297)). Purchases need my yes ([14:50](https://youtu.be/UBX3qXaFlgw?t=890)).

These are my rules, not yours. Fill in this template before you hand anything over, and revisit it whenever you add a connector or a routine. **Treat the setup as a starting point and decide your own approval rules before you hand anything over.**

## 1. The four levels

| Level | Meaning |
|---|---|
| **A. Runs alone** | The bot just does it. Only for low-risk work that changes nothing outside the chat. |
| **B. Draft first** | The bot prepares it and shows me. Nothing leaves until I say yes. |
| **C. Needs my yes** | The bot asks for my approval for this exact action before it does it. |
| **D. Never** | The bot must not do this at all, even if I ask in a hurry. |

## 2. Fill it in

Put one letter (A, B, C or D) in the last column. The "Suggested" column is where I'd start; change it if your situation differs.

| Action | Suggested | Your level |
|---|---|---|
| Summaries (morning, weekend, meeting) | A | [ ] |
| Research and reading documents | A | [ ] |
| Reminders to me | A | [ ] |
| Price checks and watch lists | A | [ ] |
| Saving records in my notes app (my own database) | A | [ ] |
| Saving a document in my file storage | A | [ ] |
| Proposing calendar entries | A | [ ] |
| Adding or moving calendar entries | C | [ ] |
| Writing an email reply | B | [ ] |
| Sending an email | C | [ ] |
| Messaging someone else | C | [ ] |
| Unsubscribing, archiving or deleting email | C | [ ] |
| Filling a shopping basket (not paying) | B | [ ] |
| Buying or checking out | C | [ ] |
| Booking, reserving or cancelling anything | C | [ ] |
| Entering or storing payment details | D | [ ] |
| Connecting a bank account | D | [ ] |
| Moving money or paying a bill | D | [ ] |
| Sharing my documents or details with anyone | D | [ ] |
| [Your own line] | | [ ] |

Notes on my own choices, so you can decide yours:

- In my setup, calendar updates happen when I tell the bot about a change. A stricter default is level C; the table suggests that.
- I keep my bank accounts disconnected and pull spending data through a separate budgeting app ([01:50 in the video](https://youtu.be/UBX3qXaFlgw?t=110)). Whether you connect anything financial is your call.
- In the video I mention that I have a card linked and the shopper can check out after my approval, or I buy it myself ([14:50](https://youtu.be/UBX3qXaFlgw?t=890)). The suggested level here is "I buy it myself" until you've watched the shopper work for a while.

## 3. Rules block to paste into your primary bot

Fill in the square brackets from your table, then paste this into the primary bot prompt (or say "add these to your standing rules").

```
Approval rules. These apply to every bot and every routine, and they override anything else I ask in a hurry.

Runs alone (no approval needed): [list, e.g. summaries, research, reminders to me, price checks].
Draft first (prepare it, show me, send nothing): [list, e.g. email replies, grocery basket, weekend plan].
Needs my yes for that exact action: [list, e.g. sending an email, adding or moving calendar entries, buying, unsubscribing].
Never, even if I ask: [list, e.g. entering payment details, connecting a bank account, moving money, sharing my documents].

Always:
- Drafts come to me first. Nothing is sent, posted or shared until I've seen it and said yes.
- Anything that spends money, books or cancels needs my yes to the exact item and price.
- If an approval request is unanswered, don't act. Ask again later and keep a list of what is waiting.
- If you are unsure which level applies, treat it as "needs my yes".
- Tell me what you did after every action that changed something outside this chat.
- Keep my private information private.
```

## 4. Review

Once a month (or when something changes):

- Read the Routines list for each bot and check each routine still matches its level.
- Check which connectors are still connected and remove any you don't use.
- Look at what was waiting for approval and whether the rules should change.
