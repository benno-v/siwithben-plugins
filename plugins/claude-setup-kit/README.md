# Claude Setup Kit (Claude Code & Cowork plugin)

Set Claude up properly in 7 steps, then keep it that way: fill-in templates for each level of instructions, a skill that creates a ready-to-use project folder, and a skill that checks your setup and tells you what to fix.

I made this to go with my video on setting up Claude in 7 steps. Most people install Claude, type a question and never touch the settings. A few minutes on instructions, folders and skills makes every answer after that more useful.

*By Benjamin Vermeulen, [@SIwithBen](https://www.youtube.com/@SIwithBen).*

Featured in: [my video on setting up Claude in 7 steps](https://youtu.be/b1cURUk9C4Y) and [Simple guide to setup Claude Cowork for your projects](https://youtu.be/pmQO4wLXspI)

## Install

Works in **Claude Code** and **Claude Cowork** (paid Claude plans: Pro, Max, Team, Enterprise). Adding the marketplace only lists the plugins; you then install just the one you want.

### Claude Code

```
/plugin marketplace add benno-v/siwithben-plugins
/plugin install claude-setup-kit@siwithben-plugins
```

In a session, `/plugin install` opens the plugin's details so you can pick a scope (just you, this project, or this repo only). From a terminal: `claude plugin marketplace add benno-v/siwithben-plugins` then `claude plugin install claude-setup-kit@siwithben-plugins`. Newer Claude Code versions can do both in one step: `/plugin install claude-setup-kit --marketplace benno-v/siwithben-plugins`.

To get future updates, run `/plugin`, open **Marketplaces**, select `siwithben-plugins` and choose **Update marketplace** (or **Enable auto-update**; it is off by default for non-Anthropic marketplaces).

### Claude Cowork (and the Claude desktop/web app)

1. In the Claude desktop app, open the **Cowork** tab, then **Customize** in the left sidebar.
2. Go to **Plugins** > **Add** > **Add marketplace** > add from a repository.
3. Enter `benno-v/siwithben-plugins` (or `https://github.com/benno-v/siwithben-plugins`).
4. Each plugin in the marketplace is listed separately: find **claude-setup-kit** and click **Install**.

Plugins added this way are saved to your Claude account, so their skills also show up in Claude chat and (same account) in Claude Code. Use **Check for updates** on the marketplace, or turn on **Sync automatically**.

Team/Enterprise owners can sync this repo for the whole organisation under **Organization settings > Plugins & skills > Marketplaces** (organisation marketplaces must be private or internal repos).

## The 7 steps

1. **Review your settings**: memory on, code execution and file creation on, web search on, reference past chats, fill in your profile, and make a deliberate choice on privacy / model training.
2. **Connect the apps you use most**, not everything.
3. **Pick where you run Claude**: web or desktop chat for quick questions, Cowork for multi-step work on your files, Claude Code for repos and scripts.
4. **Set up files and projects**: one main folder Claude can access, with a subfolder per project or client. Projects keep knowledge, instructions and memory together; local folders are better for bigger multi-step work and drafts. Only carry forward what matters, to save usage.
5. **Teach Claude about you** with the three instruction levels below.
6. **Add skills**, from the library or your own (like the two in this plugin).
7. **Set model, effort and autonomy per task**: a bigger model and higher effort for complex work, lighter for brainstorming. Keep an eye on your usage limits.

## Where each level of instructions lives

| Level | What goes in it | Claude app (chat and Cowork) | Claude Code |
|---|---|---|---|
| Global | Who you are, your role, industry and experience; how to answer (length, structure, tone, spelling); what NOT to do | Settings > General > "Instructions for Claude". Applies to every conversation; in the new experience this also covers Cowork (older Cowork builds: Settings > Cowork > Global instructions). [Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) | `~/.claude/CLAUDE.md` (you, all projects). [CLAUDE.md docs](https://code.claude.com/docs/en/claude-md) |
| Project | One client or project: formatting rules, terminology, reporting style | The Instructions of a Project (claude.ai Projects and Cowork projects), plus its knowledge or folders and project memory. [Projects](https://claude.com/docs/cowork/guide/projects) | `./CLAUDE.md` or `./.claude/CLAUDE.md` in the project. [CLAUDE.md docs](https://code.claude.com/docs/en/claude-md) |
| Folder | How to work in this folder: what is where, where drafts go | Cowork folder instructions, when you select a local folder (Customize panel) | A `CLAUDE.md` in a subfolder, loaded when Claude works there. [CLAUDE.md docs](https://code.claude.com/docs/en/claude-md) |

**Instructions vs memory.** Memory learns from your past chats, so it can keep doing old things. Instructions are what you decide now. When a habit is wrong, correct it in your instructions on purpose.

**Negative instructions carry weight.** "Do not use em dashes" works better than hoping Claude picks up your style. Review your instructions from time to time and remove what is no longer true.

## Templates

In [`templates/`](templates). Each starts with a one-line "Where this goes" pointer.

| Template | Use it for |
|---|---|
| [global-instructions.md](templates/global-instructions.md) | Your about-me and global instructions, with a "what not to do" section and a filled-in example for a fictional project manager. Keep it under about 1,500 characters. |
| [project-instructions.md](templates/project-instructions.md) | One client or project: formatting, terminology and reporting rules |
| [folder-CLAUDE.md](templates/folder-CLAUDE.md) | A `CLAUDE.md` for a project folder (the `pm-project-init` skill fills this in for you) |

Open the template, copy the block, replace everything in [brackets] and delete what does not apply. Then paste it where the table above says.

## Skills

| Skill | Command | What you get |
|---|---|---|
| PM project init | `/claude-setup-kit:pm-project-init` | A project folder with phase folders, `inputs/`, `outputs/`, `archive/`, a filled-in `CLAUDE.md` and starter brief, stakeholders, glossary and decisions log. Never overwrites anything. |
| Setup check | `/claude-setup-kit:setup-check` | A scorecard of your setup against the 7 steps, your top 3 improvements and suggested rewritten instruction text. Only proposes; changes nothing. |

### PM project init

> Set up a project folder for the Website Relaunch, sponsor is the Chief Digital Officer, ends in June, in my PM Projects folder.

Claude asks once for anything missing (unknowns are fine and become "[to confirm]"), shows a dry run, then creates:

```
PM Projects/
  website-relaunch/
    CLAUDE.md
    context/  project-brief.md  stakeholders.md  glossary.md  decisions-log.md
    01-initiation/  02-planning/  03-execution/  04-monitoring-and-control/  05-closure/
    inputs/   raw notes and transcripts
    outputs/  drafts Claude produces
    archive/
```

Run it again and it creates nothing new: existing files are skipped and listed, existing folders are reused. To change an existing `CLAUDE.md`, Claude proposes a diff and waits for your approval.

You can also run the script yourself (Python 3, no installs):

```
python3 skills/pm-project-init/scripts/init_pm_project.py --root "PM Projects" --name "Website Relaunch" --sponsor "Chief Digital Officer" --dry-run
```

### Setup check

> Check my Claude setup.

Claude reads what it can (in Claude Code or Cowork with folder access) and asks you to paste the rest: your global instructions, one project's instructions, a `CLAUDE.md`, your folder tree, your skills and connectors, and your model habits. You get a table like this:

| Step | Status | Evidence | The one fix |
|---|---|---|---|
| 5. Instruction levels | Could improve | Global instructions mention one client's report format | Move the report format into that client's Project instructions |
| 4. Files and projects | Missing | All files in one flat folder | Create one main folder with a subfolder per project |
| 2. Connected apps | Not checked | Not shared | Share which connectors are on |

Anything it could not see is marked Not checked rather than guessed.

## Watch

- [The 7 steps, general settings and global instructions (03:56)](https://youtu.be/b1cURUk9C4Y?t=236)
- [Folder structure (13:30)](https://youtu.be/b1cURUk9C4Y?t=810)
- [Instruction levels: global, project and folder (17:10)](https://youtu.be/b1cURUk9C4Y?t=1030)
- [One main "PM Projects" folder with a folder per project (01:05)](https://youtu.be/pmQO4wLXspI?t=65)

## Always review

SI output is a draft. You are the final quality gate: check every instruction and file before you rely on it, and review your setup again every few months.

## License

MIT
