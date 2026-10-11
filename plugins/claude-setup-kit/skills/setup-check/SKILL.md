---
name: setup-check
description: Review the user's current Claude setup against 7 steps (settings, connected apps, where Claude runs, files and projects, instruction levels, skills, model and effort) and return a scorecard, the top 3 improvements and suggested rewritten instruction text. Only proposes; never changes settings or files. Use when the user asks to check, audit, review or improve their Claude setup, custom or global instructions, project instructions or CLAUDE.md.
---

# Setup check

Score the user's Claude setup against the 7 setup steps and give them the few changes that will make the biggest difference.

## Ground rules

- Only propose. Never change settings, instructions, files or folders yourself, even if you have access.
- Never guess. Anything you could not see is marked **Not checked**, with what you would need to check it.
- Quote the user's own text as evidence, briefly. Never invent what their settings say.
- Ask once for what you need, then work with what you have.
- Plain British English, short bullets, no em dashes.

## Step 1: gather

If you are in Claude Code or Cowork with folder access, first read what you can: `CLAUDE.md` in the current folder and `.claude/CLAUDE.md`, `~/.claude/CLAUDE.md` if readable, the folder tree (two levels deep), and the installed skills you can see. Say what you read.

Then ask the user, in one short numbered list, to paste whatever you could not read:

1. Their global instructions (Settings > General > "Instructions for Claude", or `~/.claude/CLAUDE.md`)
2. The instructions of one Project they use a lot
3. A project folder's `CLAUDE.md` (or Cowork folder instructions)
4. Their folder tree (top two levels)
5. Which connectors / apps and skills they have turned on
6. Which settings are on: memory, reference past chats, code execution and file creation, web search, profile, and their privacy / model training choice
7. Where they mostly use Claude (web, desktop, Cowork, Code) and their model habits (which model and effort for which kind of task, and whether they hit usage limits)

Say they can skip any item; it will be marked Not checked.

## Step 2: check against the 7 steps

| # | Step | What good looks like |
|---|---|---|
| 1 | Review settings | Memory on, reference past chats on if wanted, code execution and file creation on, web search on, profile filled in, privacy / model training choice made deliberately |
| 2 | Connect apps | The few apps they use most are connected (e.g. email, calendar, drive); nothing connected "just in case" |
| 3 | Where Claude runs | A clear choice per kind of work: chat (web/desktop) for quick questions, Cowork for multi-step work on files, Code for repos and scripts |
| 4 | Files and projects | One main folder Claude can access with one subfolder per project or client; Projects hold knowledge, instructions and memory; drafts live in the folder (e.g. `outputs/`), not in the Project; only what matters is carried forward |
| 5 | Instruction levels | Global = who they are and how to answer, with a "what not to do" list; Project = client formatting, terminology, reporting; Folder = short, current `CLAUDE.md`; no contradictions between levels; habits corrected in instructions, not left to memory |
| 6 | Skills | Repeated tasks turned into skills (from the library or their own) |
| 7 | Model, effort, autonomy | Bigger model / higher effort for complex work, lighter for brainstorming and quick tasks; aware of usage limits; autonomy set to match the risk of the task |

Look in particular for:

- Project-specific detail (client names, one client's formatting) in global instructions
- No negative instructions ("Do not ...") anywhere
- Contradictions between levels (e.g. global says "short answers", project says "full detail always")
- Global instructions much longer than about 1,500 characters
- `CLAUDE.md` too long (more than about one screen), stale (old dates, finished phases, people who left) or repeating the global instructions
- Drafts and old versions stored in the Project knowledge instead of the folder
- No per-project folders, or everything in one flat folder
- Relying on memory to fix a habit instead of writing an instruction

Status values: **Good**, **Could improve**, **Missing**, **Not checked**.

## Output format

```
# Claude setup check
Based on: <what you read or were given>

## Scorecard
| Step | Status | Evidence | The one fix |
|---|---|---|---|
| 1. Settings | <status> | <short quote or observation, or "not shared"> | <one action> |
| 2. Connected apps | ... | ... | ... |
| 3. Where you run Claude | ... | ... | ... |
| 4. Files and projects | ... | ... | ... |
| 5. Instruction levels | ... | ... | ... |
| 6. Skills | ... | ... | ... |
| 7. Model, effort, autonomy | ... | ... | ... |

## Top 3 improvements
1. **<change>**: <why, one sentence> <where to do it>
2. ...
3. ...

## Suggested instruction text
### Global instructions (Settings > General > "Instructions for Claude")
<rewritten text, under about 1,500 characters, with a "What not to do" section>

### Project instructions (<project name>)
<rewritten text, or "Not checked">

### CLAUDE.md (<folder>)
<rewritten text, or "Not checked">

## Not checked
- <item>: <what to share so it can be checked>
```

Only include a rewritten level if you saw the original or the user asked for a fresh one; otherwise write "Not checked". Keep each rewrite shorter than the original where possible, and move detail to the right level rather than deleting it.

## Before handing over

End with one line: "Nothing has been changed. Copy the parts you agree with into the right place, and review your instructions again in a few months."
