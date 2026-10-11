# Claude setup check
Based on: your pasted global instructions, Contoso Project instructions, Project knowledge summary, folder description, skills, connectors and model habits. I could not read any files or settings directly.

## Scorecard
| Step | Status | Evidence | The one fix |
|---|---|---|---|
| 1. Settings | Not checked | Not shared | Share which settings are on (see Not checked below) |
| 2. Connected apps | Could improve | "Connectors: Gmail" | If you use a calendar or drive for reporting every day, connect those as well. Don't connect anything else. |
| 3. Where you run Claude | Not checked | Not shared | Tell me where you mostly use Claude (web, desktop, Cowork, Code) |
| 4. Files and projects | Could improve | "46 files incl. 30 drafts"; "everything in Desktop/Claude stuff/ (no per-project folders)" | Remove the drafts from the Project knowledge and give each project its own folder with an `outputs/` subfolder |
| 5. Instruction levels | Could improve | "Be thorough and detailed. Keep answers short."; global "American spelling" and Contoso "British spelling"; Contoso detail sits in the global instructions; no "Do not" lines | Move the Contoso detail into the Project, settle on one default answer length and add a "What not to do" list |
| 6. Skills | Missing | "Skills: none"; "Weekly report for Contoso goes out Fridays" | Turn the weekly Contoso status report into a skill |
| 7. Model, effort, autonomy | Could improve | "always the biggest model on max effort, even for quick brainstorming; hits usage limits most weeks" | Use a lighter model and lower effort for brainstorming and quick tasks. Save max effort for reports and charters. |

## Top 3 improvements
1. **Fix the contradictions and move Contoso detail out of the global instructions**: "thorough and detailed" and "keep answers short" pull Claude in opposite directions, and the Contoso colours, gates and Friday report currently apply to every chat. Do this in Settings > General and in the Contoso Project instructions.
2. **Clear the drafts out of the Contoso Project and set up per-project folders**: 30 old versions (status-report-v1 to v12, charter-draft-1 to 6) can lead Claude to quote out-of-date content. Keep only the latest final versions in the Project knowledge. Store the drafts in something like `Desktop/Claude/Contoso/outputs/`.
3. **Match the model and effort to the task**: you hit usage limits most weeks, and brainstorming does not need max effort. Pick the model and effort when you start each chat.

## Suggested instruction text
### Global instructions (Settings > General > "Instructions for Claude")
```
About me
I'm a project manager at a logistics company. I write status reports, project charters and plans.

How to answer
- Keep answers short by default: lead with the answer, then a few bullets.
- Give full detail only when I ask for it, or when a decision depends on it.
- Use American spelling unless a Project says otherwise.
- If my request is unclear, ask one question before starting.

What not to do
- Do not add background or caveats I did not ask for.
- Do not invent figures, dates or names; flag what is missing instead.
- Do not use jargon without a short explanation.
- Do not repeat my question back to me.
```

### Project instructions (Contoso)
```
Contoso account
- Use British spelling for everything in this Project.
- Tone: friendly and professional.
- Status ratings: use Contoso's red/amber/green colours.
- Call milestones "gates".
- The weekly status report goes out every Friday.

What not to do
- Do not use the word "milestone"; always say "gate".
- Do not use older drafts in the knowledge as the current position; use the latest final version only.
```
Check the spelling choice: I have kept American as your default and British for Contoso. If you want British everywhere, change the global line.

### CLAUDE.md (no folder)
Not checked. You have no `CLAUDE.md` yet. Ask for a starter version once the per-project folders are set up.

## Not checked
- **Settings:** say whether these are on: memory, reference past chats, code execution and file creation, web search and profile. Also share your privacy and model training choice.
- **Where you run Claude:** say whether you mostly use web, desktop, Cowork or Code, and for which kinds of work.
- **Autonomy:** say how much you let Claude act on its own, for example sending emails through Gmail or editing files.
- **Other apps you use daily:** list any calendar, drive or task tool you use, so I can check whether connecting it would help.

Nothing has been changed. Copy the parts you agree with into the right place, and review your instructions again in a few months.
