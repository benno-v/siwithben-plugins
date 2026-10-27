# Changelog

All notable changes, per plugin. Versions follow [semantic versioning](https://semver.org/): MAJOR for changes that break how people use a plugin, MINOR for new skills or features, PATCH for wording fixes. Release tags are `<plugin>-v<version>`, e.g. `pm-toolkit-v0.2.0`.

## pm-toolkit

### 0.3.0 (2026-10-11)
- Add gantt-chart skill: collects tasks from a pasted list, a CSV/Excel file or a connected PM tool (read only), normalises them to a task JSON schema and renders an interactive self-contained HTML chart, an Excel workbook with conditional-formatting bars that follow edited dates, and a 16:9 PowerPoint deck.
- Never invents dates or durations: tasks without enough data are listed under "Unscheduled, needs dates". Finish-to-start scheduling from dependencies, critical path by total float, calendar or working days, and checks for circular or unknown dependencies, end before start and missing owners.
- Python scripts (standard library plus openpyxl and python-pptx), three sample plans and unit tests; tests run in CI.

### 0.2.0 (2026-10-11)
- Add four day-to-day project skills: project-summary, weekly-priorities, risk-update and stakeholder-email.
- risk-update verifies a risk ID against its description before editing and never edits a register without the user confirming the change first.

### 0.1.0 (2026-10-11)
- First release: project-charter, wbs-estimate, risk-register and exec-translator skills.
- Documented installation in Claude Cowork and Claude Code.

## task-tracker

### 0.1.0 (2026-10-11)
- First release: one TASKS.md (Open, Proposed needs approval, Done, Change log; ID, Action, Owner, Source, Raised, Due, Status, Notes) as the single source of truth.
- sweep skill: reads Gmail, Google Calendar, Slack, Notion, ClickUp and meeting notes since the last sweep, keeps committed actions only, de-duplicates across sources and against existing rows, puts inferred or ambiguous-owner items in Proposed with a reason, never changes an owner or due date silently, and in scheduled mode only adds Proposed rows. Validation checkpoint before anything goes into a status report.
- morning-brief skill (read only, never sends) and dashboard skill: self-contained HTML with KPI cards, tick boxes for open tasks only, inline edits, an approval panel with Approve, Reject and Edit and no tick boxes, and Copy changes / Download changes. Pasted changes are applied by script with a revision check over the task rows, per-row snapshot checks, dry run, change log and the last 5 timestamped backups; the same block is never applied twice, and nothing is written with duplicate IDs or if TASKS.md changed during the apply. Optional mirror to a Notion database on request.
- Python 3 standard library scripts (tasks_md.py, render_dashboard.py, apply_changes.py), paste-ready Cowork scheduled tasks, SETUP-PACK.md, fictional five-source sample data and unit tests; tests run in CI.

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

## kits/grok-bot-personal-assistant

### 1.0.0 (2026-10-27)
- First release: the setup from the video "How I Use GrokBot as My Personal Assistant" as generic prompts. Primary-bot setup prompt that interviews you first, one prompt for each of six sub-bots (fitness coach, food bot, money bot, inbox bot, research bot, personal shopper), the 12 jobs as ready-to-paste prompts, eleven routine templates with plain-English schedules and cron-style notation, an approval-rules template with a paste-ready rules block, and a connector setup checklist (Gmail, Google Calendar, Google Drive, Notion, budgeting app, Grok's own computer) with a test for each step.
- Holds no private details. Money bot never connects to a bank account or moves money; shopper never checks out without a yes to the exact item and price.
- Tests: tests/test_kit.py (structure, 12 jobs, routine format, approval wording, no private data, SI branding, link and timestamp checks) runs in CI; dry-run evidence in tests/evidence.

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
