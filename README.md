# SI with Ben: plugins for Claude Code and Claude Cowork

I make practical plugins for project managers and busy professionals, to go with my YouTube channel [SI with Ben](https://www.youtube.com/@SIwithBen). Every plugin here works in **Claude Code** and **Claude Cowork**.

*By Benjamin Vermeulen, @SIwithBen.*

| Plugin | What it does |
|---|---|
| [pm-status-report](plugins/pm-status-report) | Rough notes → consistent weekly status report with RAG rating |
| [pm-toolkit](plugins/pm-toolkit) | Charter, WBS + PERT, risk register, exec translator, project summary, weekly priorities, risk update, stakeholder email |
| [ai-pm-project-plan](https://github.com/benno-v/ai-pm-project-plan) | Client-ready Gantt with milestones, tracker and status snapshot as HTML, PowerPoint, Excel and PDF (lives in its own public repo) |

## Install one plugin

Adding the marketplace only lists the plugins. Then install just the ones you want.

**Claude Code**

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install pm-toolkit@siwithben-plugins
```

Swap `pm-toolkit` for `pm-status-report` (or install both). Terminal equivalent: `claude plugin marketplace add benno-v/siwithben-plugins` then `claude plugin install pm-toolkit@siwithben-plugins`.

**Claude Cowork**

1. In the Claude desktop app, open the **Cowork** tab, then **Customize**.
2. **Plugins** → **Add** → **Add marketplace**, and enter `benno-v/siwithben-plugins`.
3. Each plugin is listed separately; click **Install** on the one you want.

Plugins added in Cowork are saved to your Claude account, so their skills also work in Claude chat and in Claude Code (same account). Requires a paid Claude plan.

## For organisations

Team/Enterprise owners can sync this repository as an organisation marketplace (Organization settings → Plugins & skills → Marketplaces → Sync from GitHub). Note that organisation marketplaces must use a private or internal repo, so fork or mirror it privately.

## Feedback and changes

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md). Found a problem or have an idea? [Open an issue](../../issues/new/choose); I read every one.

## License

MIT — see [LICENSE](LICENSE).
