---
name: pm-project-init
description: Create a ready-to-use project management folder for working with Claude, with phase folders, inputs, outputs, archive, a filled-in CLAUDE.md and starter context files (brief, stakeholders, glossary, decisions log). Never overwrites existing files. Use when the user wants to set up, start, scaffold or organise a new project or client folder, or asks for a CLAUDE.md for a project.
---

# PM project init

Set up one project folder so Claude always has the right context: a short CLAUDE.md, a `context/` folder with the source-of-truth files, and clear places for raw inputs and drafts.

## Ground rules

- Never delete, move or edit an existing file. The script only creates what is missing; existing files are skipped and existing folders are reused.
- To change an existing `CLAUDE.md` (or any other existing file), show the proposed change as a diff, explain it in one line, and wait for the user to approve before writing anything.
- Never invent names, dates or goals. Anything the user does not know is written as "[to confirm]".
- Ask once, in one short numbered list, then get on with it.
- Plain British English, short sentences, no em dashes.

## Step 1: ask

Ask for the project name first. Then, in the same short numbered list, ask briefly for:

1. Sponsor
2. Project manager
3. Start and end dates
4. Goal (one sentence)
5. Key stakeholders (name and role, separated by semicolons)
6. Client terminology or reporting rules (e.g. "say workstream, not track; weekly RAG report on Fridays")
7. Where to create it. Default: the current folder. Recommend one main folder, for example `PM Projects`, that Claude has access to, with one subfolder per project or client.

Say that "don't know" is fine for anything except the name; it will be written as "[to confirm]". If the user already gave some of these, do not ask again.

## Step 2: preview, then create

The script is at `skills/pm-project-init/scripts/init_pm_project.py` inside this plugin (in Claude Code: `${CLAUDE_PLUGIN_ROOT}/skills/pm-project-init/scripts/init_pm_project.py`). It needs only Python 3.

1. Run it with `--dry-run --json` first and show the user the folder path and the list of what would be created and what already exists.
2. If the user confirms, run the same command without `--dry-run`.

```
python3 "<script path>" --root "<parent folder>" --name "<project name>" \
  --sponsor "<sponsor>" --pm "<project manager>" --start "<start>" --end "<end>" \
  --goal "<goal>" --stakeholders "<name (role); name (role)>" \
  --terminology "<rule; rule>" --reporting "<rule; rule>" --json
```

Leave out any option the user did not answer; the script fills it with "[to confirm]". If the script refuses the name (empty after cleaning, or containing `/`, `\` or `..`), ask for a different name.

If you cannot run code (for example in Claude chat without code execution or file creation), do not pretend you ran it. Instead give the user the folder list below and the filled-in `CLAUDE.md` text to create by hand.

## What gets created

```
<parent folder>/<project-name-slug>/
  CLAUDE.md                  short instructions Claude reads when it works in this folder
  context/project-brief.md   sponsor, PM, dates, goal, scope, milestones, budget
  context/stakeholders.md    stakeholder table
  context/glossary.md        client terms and words to avoid
  context/decisions-log.md   one line per decision
  01-initiation/  02-planning/  03-execution/  04-monitoring-and-control/  05-closure/
  inputs/README.md           raw notes and transcripts go here
  outputs/README.md          drafts Claude produces go here
  archive/
```

## Output format

After the real run, report back like this:

```
## Project folder ready: <project name>
Location: <full path>

**Created (<n>):** <list>
**Skipped, already there and left unchanged (<n>):** <list or "none">
**Reused folders (<n>):** <list or "none">

**Still to confirm:** <every field written as [to confirm], or "nothing">

**Next steps**
1. Give Claude access to the main folder (Cowork: select it as the working folder; Claude Code: open a session in it).
2. Fill in the [to confirm] items in CLAUDE.md and context/.
3. Put raw notes and transcripts in inputs/; ask for drafts to be saved in outputs/.
```

If an existing `CLAUDE.md` was skipped and the new details differ from it, add: "Your existing CLAUDE.md was left unchanged. Want me to propose a diff with the new details?" Only write it after the user approves the diff.

## Before handing over

End with one line: "Check the brief and stakeholder list against what you actually know, and keep CLAUDE.md short; move detail into context/."
