# PM Toolkit (Claude Code & Cowork plugin)

Eight everyday project management skills that give you consistent, ready-to-review documents in seconds.

I built these from the prompts I use most as a project and programme manager, and show them in my videos.

*By Benjamin Vermeulen, [@SIwithBen](https://www.youtube.com/@SIwithBen).*

Featured in: [5 ChatGPT Prompts Every Project Manager Needs](https://www.youtube.com/watch?v=480NbXPA5q8), [How to create a Project Charter](https://www.youtube.com/watch?v=nnqyx-8pIVM) and [Simple guide to setup Claude Cowork for your projects](https://youtu.be/pmQO4wLXspI)

## Install

Works in **Claude Code** and **Claude Cowork** (paid Claude plans: Pro, Max, Team, Enterprise). Adding the marketplace only lists the plugins; you then install just the one you want.

### Claude Code

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install pm-toolkit@siwithben-plugins
```

In a session, `/plugin install` opens the plugin's details so you can pick a scope (just you, this project, or this repo only). From a terminal: `claude plugin marketplace add benno-v/siwithben-plugins` then `claude plugin install pm-toolkit@siwithben-plugins`. Newer Claude Code versions can do both in one step: `/plugin install pm-toolkit --marketplace benno-v/siwithben-plugins`.

To get future updates, run `/plugin`, open **Marketplaces**, select `siwithben-plugins` and choose **Update marketplace** (or **Enable auto-update**; it is off by default for non-Anthropic marketplaces).

### Claude Cowork (and the Claude desktop/web app)

1. In the Claude desktop app, open the **Cowork** tab, then **Customize** in the left sidebar.
2. Go to **Plugins** → **Add** → **Add marketplace** → add from a repository.
3. Enter `benno-v/siwithben-plugins` (or `https://github.com/benno-v/siwithben-plugins`).
4. Each plugin in the marketplace is listed separately: find **pm-toolkit** and click **Install**.

Plugins added this way are saved to your Claude account, so their skills also show up in Claude chat and (same account) in Claude Code. Use **Check for updates** on the marketplace, or turn on **Sync automatically**.

Team/Enterprise owners can sync this repo for the whole organisation under **Organization settings → Plugins & skills → Marketplaces** (organisation marketplaces must be private or internal repos).

## Skills

| Skill | Command | What you get |
|---|---|---|
| Project charter | `/pm-toolkit:project-charter` | Purpose, SMART objectives, scope, stakeholders, requirements, constraints, assumptions, success criteria, milestones |
| WBS with PERT estimates | `/pm-toolkit:wbs-estimate` | Task breakdown with optimistic / likely / pessimistic hours, PERT totals and a confidence range |
| Risk register | `/pm-toolkit:risk-register` | Risks with likelihood/impact scores, a 3x3 risk matrix, mitigations and suggested owners |
| Executive translator | `/pm-toolkit:exec-translator` | A technical update rewritten as a 30-second exec summary with one clear decision |
| Project summary | `/pm-toolkit:project-summary` | Current phase, budget status, open risks, upcoming decisions and things to watch, read straight from your connected project folder, with a source file for every fact |
| Weekly priorities | `/pm-toolkit:weekly-priorities` | The top 3 priorities for the week from your latest status report/notes, with why each matters, its source, and what to chase |
| Risk update | `/pm-toolkit:risk-update` | Line-by-line proposed changes to an existing risk register's status, score and notes — verifies each risk ID against its description and never edits without your confirmation |
| Stakeholder email | `/pm-toolkit:stakeholder-email` | A concise draft email from this week's priorities and decisions — subject, context, decisions needed with dates, one clear ask; never sends anything |

You can also just describe what you need ("draft a charter for…", "what are the top risks for…", "where are we on this project") and Claude picks the right skill.

**Weekly status report:** that one lives in its own plugin, [pm-status-report](../pm-status-report):

```
/plugin install pm-status-report@siwithben-plugins
```

## How the skills behave

- They ask once for anything important that is missing, then get on with it.
- They never invent figures, dates or names; gaps are marked "Not provided" or "TBC".
- Output always follows the same layout, so your documents look consistent.

## Always review

SI output is a draft. You are the final quality gate: check every figure, owner and date before it goes to a sponsor or client.

## License

MIT
