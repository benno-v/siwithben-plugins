**Turn 1: what I would have asked**

Happy to set that up. First, what's the project called? Then, briefly:

1. Who is the sponsor?
2. Who is the project manager?
3. What are the start and end dates?
4. What is the goal, in one sentence?
5. Who are the key stakeholders? Give name and role, separated by semicolons.
6. Does the client have terminology or reporting rules? For example, "say workstream, not track; weekly RAG report on Fridays".
7. Where should I create it? By default it goes in the current folder. I recommend one main folder, such as `PM Projects`, that Claude can access, with one subfolder per project or client.

"Don't know" is fine for anything except the name. It will be written as "[to confirm]".

**Turn 2: done**

I ran the script with `--dry-run` first. It showed nothing would be overwritten. Your answers counted as confirmation, so I then did the real run.

## Project folder ready: Warehouse Scanner Roll-out
Location: `/tmp/tmp.ueCTIpjnj7/PM Projects/warehouse-scanner-roll-out`

**Created (15):** `01-initiation/`, `02-planning/`, `03-execution/`, `04-monitoring-and-control/`, `05-closure/`, `context/`, `inputs/`, `outputs/`, `archive/`, `context/project-brief.md`, `context/stakeholders.md`, `context/glossary.md`, `context/decisions-log.md`, `inputs/README.md`, `outputs/README.md`

**Skipped, already there and left unchanged (1):** `CLAUDE.md` (it holds only "MY OWN NOTES - keep")

**Reused folders (1):** `warehouse-scanner-roll-out/`

**Still to confirm:**
- Stakeholder names for Ops, IT and Finance. You gave the areas but no people, so the names are "[to confirm]".
- Exact start and end dates. They are recorded as "Nov 2026" and "Mar 2027".
- Stakeholder influence and how to keep each one informed.
- Background, scope, milestones and budget in the brief.
- Client terminology and reporting rules.

**Next steps**
1. Give Claude access to the main folder. In Cowork, select it as the working folder. In Claude Code, open a session in it.
2. Fill in the [to confirm] items in `CLAUDE.md` and `context/`.
3. Put raw notes and transcripts in `inputs/`, and ask for drafts to be saved in `outputs/`.

Your existing `CLAUDE.md` was left unchanged. Want me to propose a diff with the new details?

Check the brief and stakeholder list against what you actually know, and keep CLAUDE.md short; move detail into context/.
