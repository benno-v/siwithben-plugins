---
name: notes-to-tasks
description: Use when I paste messy notes, a meeting transcript, a Slack thread or an email thread and ask for the actions or tasks in it, or when the notes-to-tasks routine runs.
---

# Notes to tasks

Turn messy notes into a clean, proposed task list. Pick out only the actions someone actually committed to, merge duplicates, flag anything without an owner or a clear date, and keep ideas and maybes in a separate list for me to check. Propose only: nothing is written to a task tool and nobody is messaged until I approve in this conversation.

## When to use

- I paste notes, a meeting transcript, a Slack thread or an email thread and ask "what are the actions?", "turn this into tasks", "who's doing what?" or "add these to my action list".
- I point you at notes in a connected tool (for example a meeting notes page, a Slack channel or an email thread) and ask for the actions.
- The notes-to-tasks routine runs (see the ROUTINE section below).

## Inputs and access

- **The notes.** Pasted into the chat, or read from connected tools with read access only:
  - **Slack** (or another chat tool): the threads or channels I name.
  - **Meeting notes or transcripts:** wherever I keep them (for example Notion pages or shared documents).
  - **Email** (for example Gmail): the threads I name.
- **The date of each note.** The meeting date, message timestamp or email date. You need it to turn "tomorrow" or "Friday" into a real date. If a note has no date and I haven't given one, ask me once in a one-off run; in routine mode, keep relative wording as it is and flag it.
- **Who I am**, so "I'll do it" in my own messages becomes my name, not "me".
- **Task tool, only after approval:** my Notion **Action List** database (or the database I name) with the properties `Task`, `Owner`, `Due`, `Status`, `Priority`, `Source`, `Source link` and `Notes`, as set up in the `notion-action-list` kit. If it isn't connected, you can still propose tasks and offer a CSV.

If I've asked you to read from a tool that isn't connected or returns nothing, say so in one line. Don't work from memory or an earlier run.

## Sequence of work

1. **Read every source** in scope. Note each source's name, date and link (if it has one) and who said what. Ignore filler such as greetings, "can you hear me?", "um" and small talk.
2. **Find the commitments.** Only count something as an action when a person has committed to it or it was clearly agreed. Signals include:
   - "I'll send ...", "I will ...", "I'm on it", "leave it with me".
   - "Sam to book ...", "Priya will ...", "Action: ...".
   - "Agreed: Priya owns ...", "we agreed that ... by Friday".
3. **Separate the non-actions.** Put these in the **Not actions (check)** list, with a short reason, instead of the task table:
   - Ideas and suggestions: "we could ...", "what if we ...".
   - Unassigned wishes: "someone should ...", "it would be nice to ...".
   - Maybes and hedges: "might be worth ...", "I might have a look if I get time", "possibly".
   - Questions nobody answered or took on.
   - Passing remarks, background and status updates about work already done.
   If something agreed has no owner ("we agreed the FAQ needs updating"), it is still an action: keep it in the table and flag the owner as missing.
4. **Merge duplicates.** The same action often turns up in more than one place (said in a meeting, confirmed in Slack, repeated in an email). Merge them into one row. Keep every source in the Source column. If the sources disagree on the owner or the date, use the most recent clear statement and explain the difference in Notes.
5. **Fill in each row:**
   - **Task:** starts with a verb ("Send ...", "Book ...", "Confirm ..."). Short and specific: what, and for whom or what if that matters.
   - **Owner:** the full name of the person who committed. Write `Owner missing` if nobody did. **Never guess an owner**, not even the person who raised it or the meeting organiser.
   - **Due:** an absolute date, worked out from the relative wording using the date of the note it came from, not today's date. "Tomorrow" is the note date plus one day. "Friday" or "end of the week" is the Friday of that note's week. "Next Monday" is the Monday of the following week. "EOD" is the same day. Write dates like `Thu 15 Oct 2026`. If the wording is vague ("soon", "after the launch", "next sprint", "ASAP") or there is no date at all, keep the original wording in quotes and flag it: `"soon" (Due unclear)` or `Due missing`. Don't turn vague words into a date.
   - **Source:** which note or message it came from and who said it, for example `Slack #returns-portal, Priya Nair` or `Weekly check-in transcript, Dana Whitfield`. For merged rows, list every source.
   - **Source link:** the link to the message, page or thread if the tool gives you one. Leave it blank if not; never make up a link.
   - **Status:** `Not started`, unless the notes say it's done (`Done`), under way (`In progress`) or stuck (`Blocked`).
   - **Priority:** `High`, `Medium` or `Low` only if someone stated it, or it is clearly urgent from the notes (for example "we can't go live without this"). Otherwise leave it blank. Say why in Notes when you set it.
   - **Notes:** anything useful in one line: how you resolved a date, merged sources, disagreements, the flag reason.
6. **Count** mentions found, unique tasks after merging, tasks with Owner missing, tasks with Due unclear or missing, and items in Not actions (check).
7. **Validate** with the checklist below, then return the proposal and **stop and wait** for my approval.

## Approval rules

- **Propose only.** Until I approve in this conversation, don't create, edit or delete anything in Notion or any other task tool, and don't message, mention, assign or notify anyone (no Slack posts, no emails, no drafts to the owners).
- **How I approve:** "approve all", "approve 1, 3 and 5", or approval with edits, for example "approve 2 with owner Sam Taylor, 4 due Fri 23 Oct". Apply my edits exactly. If an edit is unclear, ask before writing.
- **Anything I don't approve isn't written.** Items in Not actions (check) are never written unless I move them into the table myself.
- Approval covers adding the approved rows to the Action List only. It doesn't cover messaging owners, editing or deleting existing rows, or changing the database's properties.

## After approval

1. **Find the database.** Use my Action List database (or the one I named). If more than one database matches, ask which one. Check it has the properties `Task`, `Owner`, `Due`, `Status`, `Priority`, `Source`, `Source link` and `Notes`. If a property is missing or has a different name, tell me and ask; don't add or rename properties.
2. **Only use confirmed dates.** If you asked me for a note's date and I haven't answered, don't assume one: leave `Due` empty for rows from that note, keep the relative wording in Notes and list them in your report.
3. **Check for duplicates first.** For each approved row, look for an existing row with the same task (same meaning, ignoring small wording differences) **and** the same owner, in any status. If you find one, skip the new row and report it. Never update or overwrite the existing row.
4. **Add the remaining rows**, one page per task, with these values:
   - `Task` (title), `Source`, `Notes` as proposed.
   - `Owner`: the name. If `Owner` is a Person property, only set it when the name clearly matches one workspace member, and tell me that Notion may notify that person; otherwise leave it empty and put the name in Notes. Leave it empty for Owner missing.
   - `Due`: the date. If the due date was unclear or missing, leave `Due` empty and keep the original wording in Notes (for example `Due unclear: "after the launch"`).
   - `Status` and `Priority`: only the values `Not started`, `In progress`, `Blocked`, `Done` and `High`, `Medium`, `Low`. Leave Priority empty if it was blank.
   - `Source link`: the full URL, or empty.
5. **Report back** in one short list: added (with numbers and task names), skipped as duplicates (with the existing row it matched), and anything that failed and why.

**No database connected:** say so in one line and offer a CSV instead. If I say yes, return it in a code block, UTF-8, with this exact header row and column order: `Task,Owner,Due,Status,Priority,Source,Source link,Notes`. Write dates as `MM/DD/YYYY` (Notion imports that format as dates), leave unclear dates and missing owners empty with the reason in Notes, and wrap any value that contains a comma in double quotes. Include approved rows only.

## How to validate before returning

- Every row in the table is a commitment or a clearly agreed action. Ideas, maybes, questions and remarks are in Not actions (check), each with a reason.
- No action appears twice; merged rows list every source.
- Every Task starts with a verb.
- No owner is guessed. Gaps say `Owner missing`.
- Every Due date was worked out from the note's own date. Vague wording is kept in quotes and flagged, never turned into a date.
- No Source link is invented. Priority is blank unless stated or clearly urgent.
- The counts match the table and the list.
- Nothing has been written, sent or posted.

## What to return

```
Notes to tasks: [sources checked], [date and time]

Proposed tasks ([n]), not added yet

| # | Task | Owner | Due | Status | Priority | Source | Source link | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | [Verb ...] | [Name / Owner missing] | [Thu 15 Oct 2026 / "soon" (Due unclear) / Due missing] | [Status] | [Priority or blank] | [Source, speaker] | [URL or blank] | [Notes] |

Counts: [n] mentions found, [n] unique tasks ([n] merged duplicates), [n] Owner missing, [n] Due unclear or missing, [n] not actions.

Needs your input
- #[n]: Owner missing. Who owns it?
- #[n]: Due unclear ("after the launch"). Which date?

Not actions (check) ([n])
- "[quote]" ([source, speaker]): [reason, e.g. idea, nobody committed]

Reply "approve all", "approve 1, 3, 5" or "approve 2 with owner [name]" and I'll add them to your Action List after checking for duplicates. Nothing has been added or sent.
```

Leave out any empty section.

## Stale or missing data

- **No actions found:** say so in one line, then show Not actions (check) if there's anything in it. In routine mode, stay silent if there are no actions and nothing to check.
- **A source can't be reached or has nothing for the period:** list it at the top in one line and carry on with the rest.
- **Note has no date:** keep relative wording as it is, flag it as Due unclear and say the note was undated.
- **Action List database not connected:** propose as normal; after approval, offer the CSV.

## ROUTINE

Suggested schedule: weekdays at 17:30, after the day's meetings. Paste this into a chat with the Bot that should own the routine and change the bits in square brackets.

```
Every weekday at 17:30 in my time zone ([your time zone, e.g. Europe/London]), run the /notes-to-tasks skill on today's meeting notes in [where you keep them, e.g. my Notion Meeting Notes database] and today's messages in [Slack channels, e.g. #project-x]. Read only. Use each note's own date to work out due dates. Return the proposed task table with counts, the Needs your input list and the Not actions (check) list here in this conversation. Write nothing: don't add anything to Notion or any task tool, and don't message, mention or notify anyone. Never guess an owner; flag missing owners and unclear dates. If I approve rows later in this conversation, follow the skill's after-approval steps for those rows only. If there are no actions and nothing to check, stay silent. If a source can't be reached, tell me in one line. Show me the next run time before saving the routine.
```

When the Bot confirms, check the owning Bot, schedule and time zone, input sources (meeting notes and Slack channels), expected result (a proposal in this conversation), approval boundary (nothing written or sent) and what it does when a source is missing. Then press **Test run**. A test run does real work, so it will read your real notes and messages, but it won't write anything.
