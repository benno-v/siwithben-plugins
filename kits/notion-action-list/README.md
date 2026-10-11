# Notion Action List by SI with Ben

**Download:** [notion-action-list.zip](../notion-action-list.zip) has everything in this folder (the CSV, this guide and the licence).

I made this kit so you can have a working action list in Notion in about ten minutes. It's one CSV file that becomes a Notion database with the eight properties I use for every action: what it is, who owns it, when it's due, where it came from and how it's going. It's also the database my `notes-to-tasks` Grok Bot skill writes to, so the two work together out of the box.

*By Benjamin Vermeulen, SI with Ben ([@SIwithBen](https://www.youtube.com/@SIwithBen)).*

## What it is

| File | What it's for |
|---|---|
| `action-list.csv` | The database: a header row with the eight properties and 8 fictional example rows, so you can see how the views work before you add your own actions. UTF-8, dates in MM/DD/YYYY. |
| `README.md` | This guide: import, property types, views, template and how it pairs with the Grok Bot skill. |
| `LICENSE` | MIT. |

The example rows are made up (a fictional returns portal project at Northwind Traders) and the links point to `example.com`. One row deliberately has no owner and one has no due date, so the "No owner" view has something to show.

## Import it into Notion

Notion's own guide is here: [Import data into Notion](https://www.notion.com/help/import-data-into-notion). These are the steps I follow.

### As a new database

1. In Notion, go to **Settings > Import > CSV**. Or type `/csv` in any page and choose the CSV import.
2. Upload `action-list.csv`.
3. Choose to create a **new database** and pick where it should live (a page in your workspace).
4. Check the column mapping: each CSV column should map to a property with the same name.
5. Rename the database to **Action List**. The `notes-to-tasks` skill looks for that name, though you can point it at any name.

### Into an existing database

If you already have a full-page database you'd like to use, open it and click **••• > Merge with CSV**, then upload the file.

- The CSV headers must match your property names **exactly**, including capitals and the space in `Source link`.
- Importing **adds** rows. It doesn't update rows that are already there, so importing the same file twice gives you duplicates. Check before you merge.

### Two things that trip people up

- **Keep the file UTF-8.** If you edit the CSV in a spreadsheet, save it as "CSV UTF-8", or names with accents can turn into odd characters.
- **Keep dates in MM/DD/YYYY.** Notion imports that format as dates. If you mix formats in one column (for example 10/15/2026 and 15 Oct 2026), the column comes in as text instead of a date.

## Set the property types

After import, some columns arrive as plain text. Click each property name, choose **Edit property** and set the type like this:

| Property | Type to set | Notes |
|---|---|---|
| `Task` | Title | Usually set automatically, as it's the first column. |
| `Owner` | Text | Convert it to **Person** only if every owner is a member of your workspace. CSV import doesn't reliably fill Person properties, so I import as text first and convert afterwards. Assigning a Person can notify them. |
| `Due` | Date | |
| `Status` | Select | Options: Not started, In progress, Blocked, Done. Or convert it to Notion's **Status** type and check each option sits in the right group (Done under Complete, Blocked and In progress under In progress). |
| `Priority` | Select | Options: High, Medium, Low. Leave it empty when there's no stated priority. |
| `Source` | Text or Select | Select works well if your sources repeat (for example "Weekly check-in notes"). |
| `Source link` | URL | |
| `Notes` | Text | |

Keep the property names exactly as they are if you use the `notes-to-tasks` skill. You can change the types as above without breaking anything.

## Delete the example rows

Once you've looked at the views, clear out the examples:

1. Open the database as a table.
2. Hover over the first row, click the checkbox (or the ⋮⋮ handle) to select it, then hold Shift and click the last row to select all 8.
3. Press **Delete** (or **Backspace**), or right-click and choose **Delete**.

The properties, option lists and views stay as they are.

## Make it a reusable template

- **Duplicate the page.** Keep one empty Action List as your master copy. For each new project, open the page and choose **••• > Duplicate**, then rename the copy. Views and property types come with it.
- **Share it as a template.** To give it to someone in another workspace, publish the page from **Share > Publish** and allow duplicating as a template. They get their own copy; nothing links back to yours.
- **Database templates for new rows.** Inside the database, click the arrow next to **New** and add a template (for example one with Status set to Not started and Priority left empty), then set it as the default. Every new action starts the same way.

## Recommended views

Add each view with **+ Add a view** at the top of the database, then set the filters, sort and grouping exactly as below. For "is not Done", if you converted Status to Notion's Status type, the filter works the same way.

| View | Layout | Filter | Sort | Group |
|---|---|---|---|---|
| **By owner** | Board (or Table) | `Status` is not `Done` | `Due` ascending | `Owner` |
| **Due this week** | Table | `Due` is within `This week` **and** `Status` is not `Done` | `Due` ascending | None |
| **No owner** | Table | `Owner` is empty **and** `Status` is not `Done` | `Due` ascending | None |
| **Overdue** (optional) | Table | `Due` is before `Today` **and** `Status` is not `Done` | `Due` ascending | `Owner` |

A few notes on the views:

- **By owner:** if Notion won't offer `Owner` as the board grouping while it's a Text property, use a table grouped by Owner, or convert Owner to Person or Select. Either way, Done items are hidden by the filter.
- **Due this week:** depending on your Notion version, the date option is labelled "Is within" or "Is relative to today". Pick **This week** in either case.
- **No owner:** this is the view I check after every meeting. With the example data it shows "Update returns FAQ page". Anything here needs a name before it goes anywhere.
- **Overdue:** rows with no due date don't show here, so check the main table for those (the example "Send updated returns figures" has none on purpose).

## Pairs with the notes-to-tasks Grok Bot skill

The [notes-to-tasks](../grok-bot-starter-skills/skills/notes-to-tasks/SKILL.md) skill in my [Grok Bot starter skills](../grok-bot-starter-skills) kit reads messy notes, meeting transcripts, Slack and email threads, and proposes a task table in exactly this column order. It only writes here after you approve in the conversation:

1. Set up this database and connect Notion to your Bot.
2. Run the skill on your notes (or let its weekday 17:30 routine do it). You get a proposed table with owners, absolute due dates, sources and flags for missing owners or vague dates. Nothing is written yet.
3. Reply "approve all", "approve 1, 3 and 5" or "approve 2 with owner [name]".
4. The skill checks this database for an existing row with the same task and owner, skips those, adds the rest and tells you what it added and skipped.

If Notion isn't connected, the skill offers the approved rows as a CSV in the same column order and date format, which you can bring in with **Merge with CSV** as above.

## Featured in

- Video: [Practical Grok Bot Examples](https://youtu.be/O5bHcw_EHQs), notes to tasks at [03:48](https://youtu.be/O5bHcw_EHQs?t=228) and [12:28](https://youtu.be/O5bHcw_EHQs?t=748)
- Notion help: [Import data into Notion](https://www.notion.com/help/import-data-into-notion)
- Channel: [youtube.com/@SIwithBen](https://www.youtube.com/@SIwithBen)

## Licence

MIT. See [LICENSE](LICENSE). Use it, adapt it, share it with your team.
