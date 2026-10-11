# Sample sent emails, replies and tasks (fictional)

Test data for `skills/follow-up-tracker`. Everything here is made up: Northwind Traders, Contoso and Fabrikam are fictional companies, and all addresses use `.example` domains.

**Mailbox owner:** Sam Taylor, Operations Lead, Northwind Traders
**Run date:** Tuesday 6 October 2026, 16:00 (Europe/London)
**Look-back:** 7 days (from Tuesday 29 September 2026)

**Expected result (for checking):**

- Waiting on others: Alex Morgan (2027 pricing, nudge drafted), Maria Santos (peak headcount, nudge drafted), Chris Dube (forklift quotes, "Nudged 5 Oct, cooling off", no new draft). Priya Nair replied, so she's not included. The thank-you to Lee Okafor asked nothing, so it's not included.
- Waiting on me: Kim Ashby (site visit date, needs Sam's decision). Dana Whitfield was answered, so she's not included.
- Due in the next 2 days: Submit Q4 forecast (due 7 Oct), Book fire marshal training (due 8 Oct, "Owner missing").
- Flagged: Update returns SOP ("Due date missing").
- Not included: Renew pallet racking inspection (due later), Close September purchase orders (done).
- Every draft starts with "DRAFT, not sent". Nothing sent.

---

## Sent emails

### Sent 1

- **To:** Alex Morgan <alex.morgan@contoso.example>
- **Sent:** Tue 29 Sep, 11:10
- **Subject:** Updated pricing for 2027 contract

Hi Alex,

Could you send the updated pricing for the 2027 contract renewal? I need it for our budget review on 13 October.

Thanks,
Sam

**Replies:** none.

---

### Sent 2

- **To:** Priya Nair <priya.nair@northwind.example>
- **Sent:** Wed 30 Sep, 09:25
- **Subject:** Overtime figures for September

Hi Priya, could you share the September overtime figures by Friday?

Sam

**Replies:**

- **From:** Priya Nair, Thu 1 Oct, 14:02: "Attached, let me know if you need the breakdown by site."

---

### Sent 3

- **To:** Maria Santos <maria.santos@northwind.example>
- **Sent:** Wed 30 Sep, 15:40
- **Subject:** Peak season headcount

Hi Maria,

Can you confirm how many temporary staff we need for peak season? Agency needs our number by 9 October.

Sam

**Replies:** none.

---

### Sent 4

- **To:** Chris Dube <chris.dube@northwind.example>
- **Sent:** Thu 1 Oct, 10:15
- **Subject:** Forklift training quotes

Hi Chris, can you send me the two quotes for the forklift refresher so I can approve the budget?

Sam

**Replies:** none.

---

### Sent 5

- **To:** Lee Okafor <lee.okafor@northwind.example>
- **Sent:** Fri 2 Oct, 16:30
- **Subject:** Thanks for sorting bay 2

Thanks Lee, really appreciate you getting the repair booked so quickly.

Sam

**Replies:** none (none expected).

---

### Sent 6 (previous nudge)

- **To:** Chris Dube <chris.dube@northwind.example>
- **Sent:** Mon 5 Oct, 09:05
- **Subject:** RE: Forklift training quotes

Hi Chris, just a gentle nudge on the two quotes when you get a moment. Thanks!

Sam

**Replies:** none.

---

## Received emails (waiting on me?)

### Received 1

- **From:** Kim Ashby <kim.ashby@fabrikam.example>
- **Received:** Thu 1 Oct, 13:20
- **Subject:** Site visit

Hi Sam, which date works for our site visit: 12 or 19 October?

Kim

**Sam's replies:** none.

---

### Received 2

- **From:** Dana Whitfield <dana.whitfield@northwind.example>
- **Received:** Fri 2 Oct, 10:00
- **Subject:** KPI pack format

Hi Sam, would you prefer the KPI pack as slides or a spreadsheet?

Dana

**Sam's replies:**

- **From:** Sam Taylor, Fri 2 Oct, 11:15: "Spreadsheet please, thanks Dana."

---

## Tasks (from the task tool)

| Task | Owner | Due | Status |
|---|---|---|---|
| Submit Q4 forecast to finance | Sam Taylor | Wed 7 Oct 2026 | In progress |
| Book fire marshal training | (none) | Thu 8 Oct 2026 | Not started |
| Update returns SOP with inspection window | Maria Santos | (none) | Not started |
| Renew pallet racking inspection | Lee Okafor | Fri 23 Oct 2026 | Not started |
| Close September purchase orders | Dana Whitfield | Mon 5 Oct 2026 | Done |
