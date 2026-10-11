# Keeping these plugins up to date

A light routine that needs no coding beyond editing text files (you can do every step in the GitHub website editor, or ask Claude to do it).

## Changing a plugin

1. Edit the skill text in `plugins/<plugin>/skills/<skill>/SKILL.md`.
2. Bump `version` in `plugins/<plugin>/.claude-plugin/plugin.json`:
   - wording fix → `0.1.0` → `0.1.1`
   - new skill or feature → `0.1.0` → `0.2.0`
   - change that breaks how people use it → `1.0.0` → `2.0.0`
   Users only receive updates when the version changes.
3. Add a line under the plugin in `CHANGELOG.md`.
4. Commit (ideally via a pull request). The **Validate plugins** check runs automatically; only merge when it is green.
5. Tag the release: `git tag pm-toolkit-v0.2.0 && git push origin pm-toolkit-v0.2.0` (or create a release on GitHub with that tag name).

## Adding a new plugin

1. Create `plugins/<new-name>/` with `.claude-plugin/plugin.json`, `skills/<skill>/SKILL.md`, `README.md`, `LICENSE` and `preview.png` (1200×630).
2. Add an entry to `.claude-plugin/marketplace.json` (the `name` must match `plugin.json`).
3. Run `claude plugin validate .` locally, install it and test each skill with sample input.
4. Add it to the table in the main `README.md` and to `CHANGELOG.md`.

## Ground rules for skills

- Written from scratch; never copy third-party code or text.
- Ask once for missing inputs; never invent figures, dates or names.
- Fixed output format; end with a review reminder.
- Credit line: "By Ben Vermeulen, @SIwithBen".

## Monthly review (15 minutes)

- Read new issues and reply or label them.
- Skim the Claude Code / Cowork plugin docs for changes.
- Re-test each plugin once in Cowork and Claude Code with a sample input.
- Check the **Actions** tab is green.
