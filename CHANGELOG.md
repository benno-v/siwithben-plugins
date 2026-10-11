# Changelog

All notable changes, per plugin. Versions follow [semantic versioning](https://semver.org/): MAJOR for changes that break how people use a plugin, MINOR for new skills or features, PATCH for wording fixes. Release tags are `<plugin>-v<version>`, e.g. `pm-toolkit-v0.2.0`.

## pm-toolkit

### 0.2.0 (2026-10-11)
- Add four day-to-day project skills: project-summary, weekly-priorities, risk-update and stakeholder-email.
- risk-update verifies a risk ID against its description before editing and never edits a register without the user confirming the change first.

### 0.1.0 (2026-10-11)
- First release: project-charter, wbs-estimate, risk-register and exec-translator skills.
- Documented installation in Claude Cowork and Claude Code.

## ai-pm-project-plan (external, benno-v/ai-pm-project-plan)

### 1.1.0 (2026-10-11)
- Listed in this marketplace via a git URL source. Release notes live in that repo's CHANGELOG (PDF output, milestones on the Gantt, robust HTML preview).

## marketplace

### 2026-10-11
- scripts/check_plugins.py accepts external github/url plugin sources; added scripts/preview/ HTML templates for 1200x630 preview images.

## pm-status-report

### 0.1.0 (2026-10-11)
- First release: status-report skill (fixed one-page layout with RAG rating).
- Documented installation in Claude Cowork and Claude Code.
