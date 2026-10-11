# PM Status Report (Claude Code & Cowork plugin)

Turn rough project notes into a consistent, executive-ready weekly status report, with an overall Red/Amber/Green rating, in the same layout every week.

I built this so my weekly status reports look the same every week, whatever state my notes are in.

*By Benjamin Vermeulen, [@SIwithBen](https://www.youtube.com/@SIwithBen).*

Featured in: [Claude for Beginners: Skills, Connectors & Plugin](https://www.youtube.com/watch?v=6T3iAzpWIKU)

## Install

Works in **Claude Code** and **Claude Cowork** (paid Claude plans: Pro, Max, Team, Enterprise). Adding the marketplace only lists the plugins; you then install just the one you want.

### Claude Code

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install pm-status-report@siwithben-plugins
```

In a session, `/plugin install` opens the plugin's details so you can pick a scope (just you, this project, or this repo only). From a terminal: `claude plugin marketplace add benno-v/siwithben-plugins` then `claude plugin install pm-status-report@siwithben-plugins`. Newer Claude Code versions can do both in one step: `/plugin install pm-status-report --marketplace benno-v/siwithben-plugins`.

To get future updates, run `/plugin`, open **Marketplaces**, select `siwithben-plugins` and choose **Update marketplace** (or **Enable auto-update**; it is off by default for non-Anthropic marketplaces).

### Claude Cowork (and the Claude desktop/web app)

1. In the Claude desktop app, open the **Cowork** tab, then **Customize** in the left sidebar.
2. Go to **Plugins** → **Add** → **Add marketplace** → add from a repository.
3. Enter `benno-v/siwithben-plugins` (or `https://github.com/benno-v/siwithben-plugins`).
4. Each plugin in the marketplace is listed separately: find **pm-status-report** and click **Install**.

Plugins added this way are saved to your Claude account, so their skills also show up in Claude chat and (same account) in Claude Code. Use **Check for updates** on the marketplace, or turn on **Sync automatically**.

Team/Enterprise owners can sync this repo for the whole organisation under **Organization settings → Plugins & skills → Marketplaces** (organisation marketplaces must be private or internal repos).

## Use

In Cowork or Claude Code, run `/pm-status-report:status-report` and paste your notes, or just ask Claude for "this week's status report" and paste what you have (tasks done, in progress, blockers, milestones, budget). Claude asks once for anything important that is missing, then writes the report.

The report always has: overall status with reason, summary, done, in progress, blockers and risks, upcoming milestones, budget and schedule, decisions needed, and next steps.

## Always review

The plugin makes your reports consistent, not automatically correct. Check owners, dates and numbers against your sources before sending.

## License

MIT
