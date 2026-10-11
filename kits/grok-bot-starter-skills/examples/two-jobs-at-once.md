# Two jobs at once

You don't have to wait for one job to finish before starting the next. In one message, you can ask your Bot for two things: one that runs in the background and one you work on together straight away.

The Bot can hand work to a helper Bot or another Bot and keep chatting with you while that work runs.

In the video I used this to research a topic in the background while the main Bot drafted a meeting agenda from my calendar and tasks: [watch at 05:14](https://youtu.be/O5bHcw_EHQs?t=314).

## What you need

- A Bot with your **calendar** connected (read access).
- A **task tool** connected if you want tasks in the agenda (for example Notion). Optional.
- Nothing extra for the research part, unless you want it to read a connected document.

## Paste-ready prompt

Change the bits in square brackets.

```
I need two things at once.

1. In the background: hand this to a helper Bot. Research [topic, e.g. "how other teams run async weekly updates"]. Give me 5 key points, each with its source, and flag anything you couldn't verify. Don't send or publish anything.

2. Meanwhile, with me here: draft an agenda for my [meeting name] on [day]. Use my calendar for the time, length and attendees, and my open tasks for the discussion items. Keep it to 5 items or fewer with a time box for each, and put decisions needed at the top. Mark it "DRAFT" and don't send the invite or email anyone.

When the research is done, tell me, and add any relevant points to the agenda as suggestions I can accept or reject.
```

## What you'll see

- The Bot confirms it has started the research in the background, then gets on with the agenda.
- You can keep chatting about the agenda (reorder items, change time boxes, cut things) while the research runs.
- When the research finishes, the Bot reports back with the findings and suggests where they fit in the agenda.
- Exactly how the background work is shown depends on your app version, so don't worry if it looks a little different from the video.

## Tips

- **Split cleanly.** Give each job its own numbered section so it's clear which is which.
- **Pick the right job for the background.** Research, summarising long documents and gathering information work well. Anything needing your judgement works better in the foreground.
- **Set boundaries on both jobs.** Say "don't send or publish anything" in both parts. Drafts stay drafts until you approve them.
- **Ask for sources.** Background research should list where each point came from, so you can check it.
- **Don't overload it.** Two jobs is a good start. Add a third only once you trust the results.
- **Use a dedicated Bot if you have one.** If you've set up a Red Team Bot (see `skills/red-team-review/SKILL.md`), you can mention it with `@` and hand the finished agenda to it for a quick review.
