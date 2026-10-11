# PM Toolkit (Claude Code plugin)

Four everyday project management skills that give you consistent, ready-to-review documents in seconds.

*By Ben Vermeulen, [@SIwithBen](https://www.youtube.com/@SIwithBen).*

Featured in: [5 ChatGPT Prompts Every Project Manager Needs](https://www.youtube.com/watch?v=480NbXPA5q8) and [How to create a Project Charter](https://www.youtube.com/watch?v=nnqyx-8pIVM)

## Install

In Claude Code:

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install pm-toolkit@siwithben-plugins
```

## Skills

| Skill | Command | What you get |
|---|---|---|
| Project charter | `/pm-toolkit:project-charter` | Purpose, SMART objectives, scope, stakeholders, requirements, constraints, assumptions, success criteria, milestones |
| WBS with PERT estimates | `/pm-toolkit:wbs-estimate` | Task breakdown with optimistic / likely / pessimistic hours, PERT totals and a confidence range |
| Risk register | `/pm-toolkit:risk-register` | Risks with likelihood/impact scores, a 3x3 risk matrix, mitigations and suggested owners |
| Executive translator | `/pm-toolkit:exec-translator` | A technical update rewritten as a 30-second exec summary with one clear decision |

You can also just describe what you need ("draft a charter for…", "what are the top risks for…") and Claude picks the right skill.

**Weekly status report:** that one lives in its own plugin, [pm-status-report](../pm-status-report):

```
/plugin install pm-status-report@siwithben-plugins
```

## How the skills behave

- They ask once for anything important that is missing, then get on with it.
- They never invent figures, dates or names; gaps are marked "Not provided" or "TBC".
- Output always follows the same layout, so your documents look consistent.

## Always review

AI output is a draft. You are the final quality gate: check every figure, owner and date before it goes to a sponsor or client.

## License

MIT
