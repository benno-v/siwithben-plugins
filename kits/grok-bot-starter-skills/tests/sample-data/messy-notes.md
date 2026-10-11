# Sample messy notes (fictional)

Test data for `skills/notes-to-tasks`. Everything here is made up: Northwind Traders, Contoso and Fabrikam are fictional companies, and all addresses and links use `.example` domains. Paste everything below the line into a chat and say: "Run /notes-to-tasks on this. I'm Sam Taylor."

**Expected result (for checking, don't paste this part):**

Today is a Tuesday. Due dates must be worked out from each note's own date (the email thread starts yesterday, Monday).

- **12 mentions, 9 unique tasks, 3 merged duplicates:**
  1. Send final returns policy wording to Contoso. Priya Nair, **this Thursday**. Merged: Slack and meeting.
  2. Book the training room for next Wednesday's customer service session. Sam Taylor, **this Friday**. Merged: meeting and email 1 (sent Monday, "by the end of the week").
  3. Test the label printers at Leeds. Lee Okafor, **tomorrow (Wednesday)**.
  4. Draft the customer service call script. Maria Santos, **next Monday**, Status **In progress** ("already started").
  5. Confirm courier collection times for the returns bay. Kim Ashby, **this Friday**, Priority **High** ("can't go live without it"). Merged: email 2 and meeting.
  6. Update the returns FAQ page. **Owner missing**, **next Friday**.
  7. Brief the warehouse team on the new returns bay layout at Thursday's huddle. **Owner missing**, **this Thursday**.
  8. Send the updated returns figures. Chris Dube, **"soon" (Due unclear)**.
  9. Set up a leadership review of the launch. Dana Whitfield, **"after the launch" (Due unclear)**, even though the go-live date is mentioned.
- **Not actions (check), 5:** QR code on the returns slip (idea), the old returns spreadsheet (someone should), live chat from Contoso (might be worth), bay signs "if I get time" (hedge), older iPads (question nobody took on).
- Priority blank on every row except 5. Status Not started except 4.
- Source links: the Slack permalink for Slack items and the notes page link for meeting items; **blank** for email-only items (no links given).
- Nothing written to Notion, nobody messaged. The proposal ends by asking for approval.
- **After "approve all"** with the Action List below connected: task 2 is skipped as a duplicate (same task, same owner); the other 8 are added. Tasks 6 and 7 have an empty Owner; tasks 8 and 9 have an empty Due with the original wording in Notes.

**Already in the Action List (for the after-approval step):**

| Task | Owner | Due | Status |
|---|---|---|---|
| Book training room for customer service session | Sam Taylor | This Friday | Not started |
| Order replacement scanner batteries | Lee Okafor | Last Friday | Done |

---

## Slack thread: #returns-portal

**Channel:** #returns-portal, Northwind Traders workspace
**Date:** today (Tuesday)
**Link:** https://northwind.slack.example/archives/C04RETURNS/p1001

**Priya Nair** 09:05
Morning all! Final returns policy wording is nearly there. I'll send it to Alex at Contoso by Thursday.

**Lee Okafor** 09:12
Nice one. I'll test the label printers at Leeds tomorrow morning before the shift starts.

**Maria Santos** 09:20
We could add a QR code to the returns slip at some point, would save people typing in the order number.

**Sam Taylor** 09:26
Good shout, let's park that for now. Separate thing: the warehouse team need to hear about the new returns bay layout before go-live. Can it go in Thursday's huddle?

**Lee Okafor** 09:31
Agreed, it should go in Thursday's huddle. Not sure who's running the huddle this week though.

**Priya Nair** 09:33
+1

---

## Meeting transcript excerpt: Returns portal weekly check-in

**Date:** today (Tuesday), 11:00 to 11:30
**Attendees:** Sam Taylor, Priya Nair, Maria Santos, Lee Okafor, Dana Whitfield
**Notes page:** https://notes.northwind.example/returns-portal/weekly-check-in

**Dana Whitfield:** Can everyone hear me? I think my mic's... okay, yes. Great.

**Sam Taylor:** Morning. Um, so go-live is still two weeks on Monday. Let's just whizz round. Priya?

**Priya Nair:** Yeah, so, the wording. I'm, I'm sending that to Contoso on Thursday, like I said in Slack.

**Sam Taylor:** Perfect. Training. I'll book the training room for the customer service session next Wednesday. I'll get that done by Friday.

**Maria Santos:** And I've already started on the call script. Happy to own that. I'll have a draft to you by next Monday.

**Sam Taylor:** Lovely, thanks Maria. Kim at Fabrikam is confirming the courier collection times by Friday. That one's urgent, we can't go live without it.

**Dana Whitfield:** What about the FAQ page? We agreed it needs updating by next Friday, didn't we?

**Sam Taylor:** Yeah, agreed. Not sure who's picking that up. Let's, um, come back to it.

**Lee Okafor:** Someone should really look at the old returns spreadsheet one day. It's a mess.

**Priya Nair:** Might be worth asking Contoso if they can do live chat as well.

**Lee Okafor:** Oh, and I might have a look at the bay signs if I get time.

**Dana Whitfield:** I'll set up a review with the leadership team after the launch.

**Sam Taylor:** Great. Right, thanks all, sorry, I've got a hard stop.

---

## Email thread: Courier collection times and returns figures

### Email 1

- **From:** Sam Taylor <sam.taylor@northwind.example>
- **To:** Kim Ashby <kim.ashby@fabrikam.example>, Chris Dube <chris.dube@northwind.example>
- **Sent:** Yesterday (Monday) 15:10
- **Subject:** Courier collection times and returns figures

Hi Kim, hi Chris,

Kim, could you confirm the courier collection times for the new returns bay? Chris, could you send me the updated returns figures for last quarter?

On my side, I'll book the training room for next Wednesday's customer service session by the end of the week.

Thanks,
Sam

### Email 2

- **From:** Kim Ashby <kim.ashby@fabrikam.example>
- **To:** Sam Taylor
- **Sent:** Yesterday (Monday) 16:45
- **Subject:** Re: Courier collection times and returns figures

Hi Sam,

The depot is redoing its rota this week. I'll confirm the collection times by end of day Friday.

Kim

### Email 3

- **From:** Chris Dube <chris.dube@northwind.example>
- **To:** Sam Taylor
- **Sent:** Today (Tuesday) 08:20
- **Subject:** Re: Courier collection times and returns figures

Hi Sam,

I'll get the updated returns figures over soon. Quick question while I think of it: do we know if the portal works on older iPads?

Chris
