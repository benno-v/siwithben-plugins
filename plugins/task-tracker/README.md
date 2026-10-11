# Task Tracker (Claude Code & Cowork plugin)

One task tracker for everything you have committed to, wherever it was said: Gmail, Google Calendar, Slack, Notion, ClickUp and your meeting notes, pulled into a single `TASKS.md` in your folder.

I built this to go with my video on building one task tracker from all your apps. Actions get agreed in a meeting, repeated in Slack and half-confirmed by email, and none of those apps knows about the others. This plugin keeps one list with the action, owner, source, date raised, due date and status, separates real commitments from passing remarks, removes duplicates, and refreshes the list without rebuilding it.

*By Benjamin Vermeulen, [@SIwithBen](https://www.youtube.com/@SIwithBen).*

Featured in: [my video on one task tracker for all your apps](https://youtu.be/3QY8_yPKpLM?t=109). Setting it up: [SETUP-PACK.md](SETUP-PACK.md) (about 20 minutes).

## Install

Works in **Claude Code** and **Claude Cowork** (paid Claude plans: Pro, Max, Team, Enterprise). Adding the marketplace only lists the plugins; you then install just the one you want.

### Claude Code

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install task-tracker@siwithben-plugins
```

From a terminal: `claude plugin marketplace add benno-v/siwithben-plugins` then `claude plugin install task-tracker@siwithben-plugins`.

To get future updates, run `/plugin`, open **Marketplaces**, select `siwithben-plugins` and choose **Update marketplace** (or **Enable auto-update**; it is off by default for non-Anthropic marketplaces).

### Claude Cowork (and the Claude desktop/web app)

1. In the Claude desktop app, open the **Cowork** tab, then **Customize** in the left sidebar.
2. Go to **Plugins** > **Add** > **Add marketplace** > add from a repository.
3. Enter `benno-v/siwithben-plugins` (or `https://github.com/benno-v/siwithben-plugins`).
4. Each plugin in the marketplace is listed separately: find **task-tracker** and click **Install**.

Plugins added this way are saved to your Claude account, so their skills also show up in Claude chat and (same account) in Claude Code. The scripts need code execution, so use Cowork or Claude Code for the sweep and dashboard.

## How it works

`TASKS.md` in your folder is the single source of truth. It has three tables with the same columns, plus a change log:

| ID | Action | Owner | Source | Raised | Due | Status | Notes |
|---|---|---|---|---|---|---|---|
| T-009 | Send signed purchase order to procurement | Mei Chen | Gmail: "Purchase order" from Mei Chen (2026-10-09); Slack: #customer-portal (2026-10-07) | 2026-10-07 | 2026-10-14 | Open | |

- **Open**: committed actions. Status is Open, In progress, Waiting or Blocked.
- **Proposed, needs approval**: anything Claude inferred rather than read as a clear commitment, such as an unclear owner or an intention that may not be a promise. The reason is in Notes.
- **Done**: Status Done, with "done YYYY-MM-DD" in Notes.
- **Change log**: one line per change made by a sweep or the dashboard.

The **Source** column is there so you can check every owner and due date against where it came from before it goes into a status report.

## Skills

| Skill | Command | What you get |
|---|---|---|
| Sweep | `/task-tracker:sweep` | New committed actions since the last sweep from your connected apps and meeting notes, de-duplicated, with anything uncertain in "Proposed, needs approval". Shows a summary first; on a schedule it only adds proposed rows. Never messages anyone, never deletes, never changes an owner or due date without asking. |
| Morning brief | `/task-tracker:morning-brief` | Overdue, due today and this week, waiting on others, what needs your approval, today's meetings with related tasks, and your top 3 for the day. Read only. |
| Dashboard | `/task-tracker:dashboard` | A visual dashboard with tick boxes and inline edits, an approval panel with Approve, Reject and Edit (no tick boxes there, because those need your input), and a Copy changes button. Paste the block back and Claude applies it to `TASKS.md` after a dry run. Optional mirror to a Notion database. |

I didn't add separate `commands/`: Claude Code's plugin docs recommend skills for new plugins, and each skill already works as a slash command (above).

## Why the dashboard gives you a block to paste

The dashboard can't write to `TASKS.md`. A dashboard page has no access to your folder, and a Claude artifact can only store text in its own artifact storage, not in browser local storage or in your files ([What are artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them), [Artifacts in Cowork](https://support.claude.com/en/articles/14729249-use-artifacts-in-claude-cowork)). So it does what the [Claude Code artifacts docs](https://code.claude.com/docs/en/artifacts.md) recommend: an export button that produces text you paste back into the session. The block carries the revision of the task rows it was made from and a snapshot of each row you touched. If a row has changed since, that change is skipped with the reason; changes to untouched rows still go through, so a scheduled sweep in between doesn't cost you your ticks. The same block is refused a second time once it's applied. More in [SETUP-PACK.md](SETUP-PACK.md#how-the-dashboard-writes-back).

## Templates

| Template | Use it for |
|---|---|
| [TASKS.md](templates/TASKS.md) | An empty tracker. The sweep creates it for you if it's missing. |
| [scheduled-tasks.md](templates/scheduled-tasks.md) | Paste-ready Cowork scheduled tasks: morning brief at 07:00 on weekdays, a Proposed-only sweep at 08:00, 12:30 and 16:30 on weekdays, and a Friday review. |

## Scripts

Python 3, standard library only, in [`scripts/`](scripts):

```
python3 scripts/tasks_md.py init --tasks TASKS.md          # empty tracker, never overwrites
python3 scripts/tasks_md.py validate --tasks TASKS.md      # duplicate IDs, bad statuses or dates, rows it can't read
python3 scripts/render_dashboard.py --tasks TASKS.md --out dashboard.html
python3 scripts/apply_changes.py --tasks TASKS.md --changes tasks-changes.json --dry-run
```

Every write keeps the previous version in `.task-tracker-backups/` (the last 5, timestamped), writes atomically through a symlinked `TASKS.md` with its permissions kept, and refuses to write if `TASKS.md` has duplicate IDs or changed while the changes were being applied. Tests and fictional sample data from five sources are in [`tests/`](tests); [expected-sweep.md](tests/sample-data/expected-sweep.md) shows what a good sweep finds.

## Watch

- [One tracker for everything (01:49)](https://youtu.be/3QY8_yPKpLM?t=109)
- [The live dashboard idea (02:26)](https://youtu.be/3QY8_yPKpLM?t=146)
- [The sources it reads (04:15)](https://youtu.be/3QY8_yPKpLM?t=255)
- [The dashboard (12:08)](https://youtu.be/3QY8_yPKpLM?t=728)
- [Tick boxes (12:49)](https://youtu.be/3QY8_yPKpLM?t=769)
- [Needs your approval: no tick box (13:46)](https://youtu.be/3QY8_yPKpLM?t=826)
- [Ticking tasks off (14:26)](https://youtu.be/3QY8_yPKpLM?t=866)
- [Coming next: an editable dashboard (17:18)](https://youtu.be/3QY8_yPKpLM?t=1038)

## Always review

SI output is a draft. Claude can read an intention as a commitment, and can attach the wrong owner when two names share a paragraph. Check every owner and due date against its source before it goes into a status report. You are the final quality gate.

## License

MIT
