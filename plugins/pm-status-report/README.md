# PM Status Report (Claude Code plugin)

Turn rough project notes into a consistent, executive-ready weekly status report, with an overall Red/Amber/Green rating, in the same layout every week.

*By Ben Vermeulen, [@SIwithBen](https://www.youtube.com/@SIwithBen).*

Featured in: [Claude for Beginners: Skills, Connectors & Plugin](https://www.youtube.com/watch?v=6T3iAzpWIKU)

## Install

In Claude Code:

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install pm-status-report@siwithben-plugins
```

## Use

Run `/pm-status-report:status-report` and paste your notes, or just ask Claude for "this week's status report" and paste what you have (tasks done, in progress, blockers, milestones, budget). Claude asks once for anything important that is missing, then writes the report.

The report always has: overall status with reason, summary, done, in progress, blockers and risks, upcoming milestones, budget and schedule, decisions needed, and next steps.

## Always review

The plugin makes your reports consistent, not automatically correct. Check owners, dates and numbers against your sources before sending.

## License

MIT
