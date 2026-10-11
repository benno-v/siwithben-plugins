# Changelog

All notable changes, per plugin. Versions follow [semantic versioning](https://semver.org/): MAJOR for changes that break how people use a plugin, MINOR for new skills or features, PATCH for wording fixes. Release tags are `<plugin>-v<version>`, e.g. `pm-toolkit-v0.2.0`.

## pm-toolkit

### 0.2.0 (2026-10-11)
- Add four day-to-day project skills: project-summary, weekly-priorities, risk-update and stakeholder-email.
- risk-update verifies a risk ID against its description before editing and never edits a register without the user confirming the change first.

### 0.1.0 (2026-10-11)
- First release: project-charter, wbs-estimate, risk-register and exec-translator skills.
- Documented installation in Claude Cowork and Claude Code.

## claude-setup-kit

### 0.1.0 (2026-10-11)
- First release: templates for global instructions, project instructions and a project folder CLAUDE.md; pm-project-init skill with a stdlib Python script that creates a PM project folder and never overwrites existing files; setup-check skill that scores a setup against the 7 steps and only proposes changes.

## ai-pm-project-plan (external, benno-v/ai-pm-project-plan)

### 1.1.0 (2026-10-11)
- Listed in this marketplace via a git URL source. Release notes live in that repo's CHANGELOG (PDF output, milestones on the Gantt, robust HTML preview).

## kits/grok-bot-starter-skills

### 1.2.0 (2026-10-11)
- Add notes-to-tasks skill: extracts only committed actions from messy notes, meeting transcripts, Slack and email threads; merges duplicates across sources; resolves relative due dates from each note's own date; flags missing owners and vague dates; lists ideas, maybes and questions separately. Proposes only; after approval adds rows to the Notion Action List (duplicate check on task and owner) or offers a CSV. Paste-ready weekday 17:30 routine that writes nothing.
- New sample data: messy-notes.md (Slack thread, meeting transcript, email thread) with 9 actions, 3 duplicates, 2 missing owners, 2 vague dates and 5 non-actions.

### 1.1.0 (2026-10-11)
- Add weekly-status-report skill: gathers the week's evidence from email, calendar, task tracker and meeting notes, drafts a DRAFT-labelled report in the pm-status-report structure (RAG with reason, done, in progress, blockers and risks, milestones, budget and schedule, decisions needed, next steps) with sources and a missing-data list. Never sends. Paste-ready Friday 14:00 routine plus an optional "send to me only" draft variant.
- Sample data now uses relative dates (today, yesterday, this Wednesday) so dry runs never trigger the stale-data warning. New weekly-status sample data.

### 1.0.0 (2026-10-11)
- First release: inbox-cleanup, follow-up-tracker and red-team-review skills (SKILL.md, approval-first, paste-ready routine prompts with suggested schedules), two-jobs-at-once example, sample data, dry-run evidence and downloadable zip.
- CI: scripts/check_kits.py now validates skill frontmatter (name matches folder, description says when to use it) and that each skill states an approval boundary.

## kits/notion-action-list

### 1.0.0 (2026-10-11)
- First release: action-list.csv (Task, Owner, Due, Status, Priority, Source, Source link, Notes; 8 fictional rows, MM/DD/YYYY dates), README with import steps, property types, example-row clean-up, template options and the By owner, Due this week, No owner and Overdue views. Pairs with the notes-to-tasks Grok Bot skill.

## kits/chatgpt-pm-prompt-pack

### 1.0.0 (2026-10-11)
- First release: custom GPT kit (name, description, 6,360-character instructions, 4 conversation starters, pm-templates.md knowledge file with charter, WBS + PERT, risk register, exec translator and weekly status templates), plain prompt-pack.md, sample inputs, test evidence and downloadable zip.
- CI: scripts/check_kits.py checks the zip is in sync and the GPT limits (instructions under 8,000 characters, description under 300, at most 4 starters).

## marketplace

### 2026-10-11
- scripts/check_plugins.py accepts external github/url plugin sources; added scripts/preview/ HTML templates for 1200x630 preview images.

## pm-status-report

### 0.1.0 (2026-10-11)
- First release: status-report skill (fixed one-page layout with RAG rating).
- Documented installation in Claude Cowork and Claude Code.
