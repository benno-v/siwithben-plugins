# Task Tracker setup pack

*By Benjamin Vermeulen, SI with Ben ([@SIwithBen](https://www.youtube.com/@SIwithBen)).*

This is how I set up one task tracker for everything I've committed to, in about 20 minutes. It goes with [my video on one task tracker for all your apps](https://youtu.be/3QY8_yPKpLM?t=109).

## What it is

Every week I agree actions in meetings, in Slack, by email and in our PM tool. None of those apps knows about the others, so the same action turns up three times and the ones that matter get lost. This plugin gives me one list:

- **One file, `TASKS.md`**, in a folder I choose. It's plain text, so I can read it, edit it and keep it in version control.
- **A sweep** that reads my connected apps and meeting notes since the last sweep and adds only real commitments, not passing remarks. It merges duplicates (the same action in a meeting note and in Slack is one task) and puts anything it isn't sure about in "Proposed, needs approval".
- **A morning brief** with what's overdue, due today and what I should focus on.
- **A dashboard** with tick boxes, inline edits and an approval panel, which hands my changes back to Claude as a block I paste in.
- **Scheduled tasks** so the list stays current without me rebuilding it.

Each task has: action, owner, source, date raised, due date and status (plus an ID and notes).

## Setup in 20 minutes

### 1. Make a folder (2 minutes)

Create one folder for the tracker, for example `Task tracker` inside your main work folder. Put meeting notes you want swept in it, or in a `meeting-notes/` subfolder. Cowork reads and writes the local folders you connect to it ([Use Claude Cowork](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)); in Claude Code, open a session in that folder.

### 2. Connect your apps (5 minutes)

In Claude, go to **Settings > Connectors** and connect what you actually use: Gmail, Google Calendar, Slack, Notion or ClickUp. You don't need all of them. Anything not connected is listed as "Not checked" in the sweep summary, never guessed. For Apple Notes you need a local connector; without one, export notes into the folder.

### 3. Install the plugin (2 minutes)

Claude Code:

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install task-tracker@siwithben-plugins
```

Cowork: **Customize > Plugins > Add > Add marketplace**, enter `benno-v/siwithben-plugins`, then **Install** on **task-tracker**.

### 4. Run your first sweep (5 minutes)

With the folder selected, ask:

> Sweep my tasks for the last 7 days.

Claude creates `TASKS.md` (it asks first), reads the last 7 days and shows a summary: new committed tasks, tasks that need your approval and why, duplicates it merged, suggested updates, things that look done, and passing remarks it didn't track. Nothing is written until you approve.

### 5. Approve and check (3 minutes)

Read the "needs your approval" list first. Fix any owner or due date, then say "approve" (or "approve all except 2"). This is also where the validation checkpoint below comes in.

### 6. Open the dashboard (2 minutes)

> Show my task dashboard.

Claude renders `dashboard.html` in the folder. In Cowork I publish it as an artifact; in Claude Code I open the file in my browser. Tick what's done, click **Edit** to change an owner, due date, status or the wording, and use **Approve**, **Reject** or **Edit** on proposed tasks. Then click **Copy changes** and paste the block back into the session. Claude does a dry run, shows the list and applies it when I say yes.

### 7. Schedule it (1 minute each)

Open [templates/scheduled-tasks.md](templates/scheduled-tasks.md) and create three Cowork scheduled tasks from it:

- **Morning brief**: weekdays at 07:00.
- **Sweep**: weekdays at 08:00, 12:30 and 16:30, in Proposed-only mode, so nothing reaches my Open list without me.
- **Friday review**: Fridays at 15:00.

Scheduled tasks only run while the Claude desktop app is open ([Use Claude Cowork](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)). If one doesn't run, nothing is lost: the next sweep reads everything since the "Last sweep" line.

## How the dashboard writes back

I wanted the dashboard to be the place I tick things off, but `TASKS.md` stays the single source of truth. Here's why it works the way it does:

- **The page can't write your files.** A Claude artifact can keep text data in its own artifact storage (personal or shared, up to 20 MB, text only), but not in the browser's local storage and not in local files. That applies to Cowork artifacts created on or after 19 August 2026 too; Cowork "live artifacts" from before that date are view only now. Sources: [What are artifacts and how do I use them](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) and [Use artifacts in Claude Cowork](https://support.claude.com/en/articles/14729249-use-artifacts-in-claude-cowork).
- **So it hands the changes back to Claude.** The [Claude Code artifacts docs](https://code.claude.com/docs/en/artifacts.md) recommend exactly this: an export control that produces text you paste back, so what you did on the page flows into the session. **Copy changes** gives you a block like this:

  ````
  ```task-tracker-changes
  {"base_revision":"e91924acdb08","generated":"2026-10-12T09:00:00Z","ops":[{"op":"complete","id":"T-003"},{"op":"update","id":"T-002","fields":{"due":"2026-10-20","owner":"Priya Nair"}},{"op":"approve","id":"T-007"}]}
  ```
  ````

  **Download changes** saves the same thing as `tasks-changes.json`; put it in the folder and ask Claude to apply the dashboard changes. Downloads are a per-account option in artifacts, so Copy is the one that always works.
- **It can't overwrite newer work.** `base_revision` is a fingerprint of the task rows when the page was made, and each change carries a snapshot of the row you touched. A sweep that only adds proposed tasks or updates "Last sweep" doesn't get in the way: your ticks on other rows still go through. If a row you changed was changed by someone else in the meantime, that change is skipped and Claude shows you what changed, so you can re-render and redo it. For an edit, only the fields changed since are skipped. The same block pasted twice is refused the second time.
- **It keeps a trail.** Every applied change is a line in the Change log section of `TASKS.md`, and the last 5 versions are kept with a timestamp in `.task-tracker-backups/` next to it. Nothing is written if `TASKS.md` changed while the changes were being applied, and a symlinked `TASKS.md` (for example into Dropbox or Obsidian) stays a link.
- **Edit changes only what you change.** A due date like "TBC" or a status that isn't in the list stays as it is unless you pick a new one.
- **Unsaved ticks.** As an artifact with storage, the page keeps your unapplied ticks in its own storage between opens, also after a re-render, except for tasks that changed in `TASKS.md` meanwhile. As a local file it keeps them only while the page is open, so copy them before you close it. It never uses browser local storage.

## Validation checkpoint

This is the one habit that makes the tracker trustworthy. Claude can read an intention ("we should look at SSO") as a commitment, and when two names share a paragraph ("Sam and Jordan, one of you will book the auditor") it can attach the wrong owner.

So before anything from the tracker goes into a status report or an email:

1. Check every owner and due date against its source. That's what the Source column is for: it says which email, thread, meeting or task it came from, with a link where there is one.
2. Anything uncertain stays in "Proposed, needs approval" until you've decided. Those tasks have no tick box on purpose: they need your input, not a tick.
3. Owners and due dates of existing tasks are never changed silently. A sweep lists them as suggested updates and waits for you.

## Watch

- [One tracker for everything (01:49)](https://youtu.be/3QY8_yPKpLM?t=109)
- [The live dashboard idea (02:26)](https://youtu.be/3QY8_yPKpLM?t=146)
- [The sources it reads (04:15)](https://youtu.be/3QY8_yPKpLM?t=255)
- [The dashboard (12:08)](https://youtu.be/3QY8_yPKpLM?t=728)
- [Tick boxes (12:49)](https://youtu.be/3QY8_yPKpLM?t=769)
- [Needs your approval: no tick box (13:46)](https://youtu.be/3QY8_yPKpLM?t=826)
- [Ticking tasks off (14:26)](https://youtu.be/3QY8_yPKpLM?t=866)
- [Coming next: an editable dashboard (17:18)](https://youtu.be/3QY8_yPKpLM?t=1038)

## Troubleshooting

| What you see | What to do |
|---|---|
| Some changes were skipped: "changed since the block was made" | Someone changed that task after you opened the dashboard. Your other changes went through. Ask Claude to re-render the dashboard and redo the skipped ones if they still apply. |
| "these ops have no before snapshot" | The block wasn't made by the dashboard and the tasks changed since. Ask Claude to rebuild it, or check the "changed since" list and say "apply anyway". |
| "TASKS.md has duplicate IDs" | Nothing was written. Run `python3 scripts/tasks_md.py validate --tasks TASKS.md`, give one of the rows a new ID, then apply again. |
| "TASKS.md changed while these changes were being applied" | A sweep or a hand edit landed at the same moment. Nothing was written; apply again. |
| A task I added by hand isn't on the dashboard | Run `validate`: rows after a blank line, without a leading `\|`, or under a heading the tracker doesn't know (such as `## Open tasks`) are listed as not parsed. Move them into the right table. |
| "This block was already applied" | Nothing to do; it's in the Change log. Re-render the dashboard to see the current state. |
| Copy changes does nothing | Some pages block the clipboard. The block is shown and selected under the Changes tray: press Ctrl+C (Cmd+C on a Mac). |
| Download changes doesn't save a file | Downloads are switched on per account for artifacts. Use Copy changes instead. |
| My ticks were gone when I reopened the page | A local `dashboard.html` (or an artifact without storage) only keeps them while it's open. Copy changes before closing, or publish it as an artifact. |
| A source shows as "Not checked" | The connector isn't connected or failed. Connect it under Settings > Connectors and sweep again. |
| The sweep missed a task | It only tracks clear commitments. If it was a passing remark, it's under "Not tracked"; ask Claude to add it, or use **Add task** on the dashboard. |
| The wrong owner on a task | Edit it on the dashboard and paste the changes back, then check its Source. If it came from a paragraph with two names, that's the validation checkpoint doing its job. |
| The scheduled sweep didn't run | Scheduled tasks need the desktop app open. The next sweep catches up from "Last sweep". |
| "the 'Open' table must have the columns ..." | A column was renamed or removed by hand. Restore the header row from [templates/TASKS.md](templates/TASKS.md). |
| I edited TASKS.md by hand and something broke | `python3 scripts/tasks_md.py validate --tasks TASKS.md` lists duplicate IDs, statuses and dates that need fixing. The last 5 versions are in `.task-tracker-backups/`. |

## Always review

SI output is a draft. You are the final quality gate: check owners and due dates against the source before they go anywhere else.
