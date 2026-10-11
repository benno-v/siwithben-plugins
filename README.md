# SI with Ben: plugins for Claude Code and Claude Cowork

Practical plugins for project managers and busy professionals, from the YouTube channel [SI with Ben](https://www.youtube.com/@SIwithBen). Every plugin works in **Claude Code** and **Claude Cowork**.

*By Benjamin Vermeulen, @SIwithBen.*

| Plugin | What it does |
|---|---|
| [pm-status-report](plugins/pm-status-report) | Rough notes → consistent weekly status report with RAG rating |
| [pm-toolkit](plugins/pm-toolkit) | Project charter, WBS + PERT estimates, risk register, executive translator |

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

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md). Found a problem or have an idea? [Open an issue](../../issues/new/choose).

## License

MIT — see [LICENSE](LICENSE).
