> Where this goes: the Instructions field of a Project (claude.ai Projects or Cowork projects), one per client or project.

# Project instructions

Project instructions hold what is true for **this** client or project only: their formatting rules, their words, their reporting style. Anything about you in general belongs in your global instructions.

Copy the block below, replace everything in [brackets] and delete lines that do not apply. Put long reference material (contracts, plans, brand guides) in the Project knowledge or folder instead of here; these instructions should stay short.

## Fill-in

```
## This project
- Project: [project name] for [client or department].
- Goal: [one sentence on what success looks like].
- Sponsor: [name, role]. Project manager: [name].
- Key dates: [start] to [end]; next milestone [milestone, date].

## Formatting rules
- Documents: [e.g. client template, headings in sentence case, numbered sections].
- Dates: [e.g. 14 March 2027, never 03/14/27].
- Numbers and money: [e.g. EUR, thousands as "k", one decimal for percentages].
- File names: [e.g. YYYY-MM-DD_document-name_v0.1].

## Terminology
- Say [client term], not [our term] (e.g. say "workstream", not "track").
- [Acronym] means [meaning].
- Never use [word or name the client dislikes].

## Reporting style
- Status reports: [e.g. weekly, Friday, one page, RAG with a one-line reason].
- Audience: [e.g. steering committee; they want decisions and risks first].
- Always include: [e.g. decisions needed, top 3 risks, next steps with owners].
- Never include: [e.g. internal costs, named blame].

## Working in this project
- Use the files in the project knowledge or folder as the source of truth; tell me when something is missing or out of date.
- Mark anything you are not sure about as "[to confirm]" instead of guessing.
```

## Tips

- Keep one Project (and one folder) per client or project, so rules for one client never leak into another.
- Only carry forward what matters: a short brief, the current plan and the latest status. Old drafts and long transcripts in the Project use up your usage limits for little benefit.
- Store drafts Claude produces in the project folder (for example `outputs/`), not in the Project knowledge.
