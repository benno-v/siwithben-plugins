# Sample inbox (fictional)

Test data for `skills/inbox-cleanup`. Everything here is made up: Northwind Traders, Contoso and Fabrikam are fictional companies, and all addresses use `.example` domains.

**Mailbox owner:** Sam Taylor, Operations Lead, Northwind Traders
**Time window:** Monday 5 October 2026, 17:00 to Tuesday 6 October 2026, 07:30 (Europe/London)

**Expected result (for checking):**

- Flagged SENSITIVE, no draft: emails 2 (security alert), 4 (HR matter) and 7 (bank details change). They can sit in Needs reply or FYI, as long as they're flagged and have no draft.
- Needs reply, with drafts: emails 1, 5 (meeting request), 6 (overdue question) and 10.
- FYI: emails 8, 9, 11, 13 and 15.
- Archive or unsubscribe candidates: emails 3 (newsletter), 12 and 14.
- Total 15. Nothing sent, archived or unsubscribed; a proposed batch waiting for approval.

---

## Email 1

- **From:** Priya Nair <priya.nair@northwind.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 17:42
- **Subject:** Warehouse rota for half-term week

Hi Sam,

Can you confirm whether we're running the reduced rota during half-term (26 to 30 Oct)? I need to let the shift leads know by Thursday so they can plan cover.

Thanks,
Priya

---

## Email 2

- **From:** Northwind IT Security <no-reply@security.northwind.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 22:15
- **Subject:** Unusual sign-in attempt on your account

We detected a sign-in attempt on your account from a new device in a location you don't normally use. If this was you, no action is needed. If this wasn't you, reset your password immediately using the link below and contact the IT service desk.

[Reset password]

---

## Email 3

- **From:** The Ops Digest <newsletter@opsdigest.example>
- **To:** Sam Taylor
- **Received:** Tue 6 Oct, 06:00
- **Subject:** This week: 7 ways to cut picking errors

Welcome to this week's Ops Digest. Seven ways to cut picking errors, a reader poll on four-day weeks, and our pick of upcoming webinars.

[Unsubscribe] [View in browser]

---

## Email 4

- **From:** Jordan Ellis <jordan.ellis@northwind.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 18:05
- **Subject:** Confidential: concern about a team member

Hi Sam,

I'd like to raise a concern about conduct in my team that I think needs to go through HR. I'd rather not put the details in email. Could we talk privately this week?

Jordan

---

## Email 5

- **From:** Alex Morgan <alex.morgan@contoso.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 19:30
- **Subject:** Quarterly review meeting

Hi Sam,

It's time for our quarterly supplier review. Would Wednesday 14 Oct at 10:00 or Thursday 15 Oct at 14:00 work for a 45-minute call? Happy to send an invite once you pick a slot.

Best,
Alex Morgan
Account Manager, Contoso

---

## Email 6

- **From:** Chris Dube <chris.dube@northwind.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 17:20
- **Subject:** RE: Forklift training budget (third ask)

Hi Sam,

Just following up again on my email from 22 Sep. I still need a yes or no on the forklift refresher training budget (four people). The provider's held price expires on Friday.

Chris

---

## Email 7

- **From:** Fabrikam Accounts <accounts@fabrikam.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 20:48
- **Subject:** Change of bank details for future payments

Dear customer,

Please note our bank details have changed. Update your records and use the new account for all invoices from today. New details attached.

Fabrikam Accounts Team

---

## Email 8

- **From:** Lee Okafor <lee.okafor@northwind.example>
- **To:** Ops Team
- **Received:** Mon 5 Oct, 17:55
- **Subject:** Loading bay 2 back in service

Hi all,

Loading bay 2 is fixed and back in service from tomorrow morning. Thanks for your patience.

Lee

---

## Email 9

- **From:** Courier Tracking <tracking@parcelco.example>
- **To:** Sam Taylor
- **Received:** Tue 6 Oct, 06:45
- **Subject:** Your parcel is out for delivery

Your parcel (ref PC-48213) is out for delivery today between 10:00 and 12:00.

---

## Email 10

- **From:** Maria Santos <maria.santos@northwind.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 21:10
- **Subject:** Draft SOP for returns: your comments?

Hi Sam,

I've attached the draft returns SOP. Could you review section 3 (damaged goods) and let me know if the two-day inspection window works for your team? I'd like to finalise it by next Monday.

Thanks,
Maria

---

## Email 11

- **From:** Northwind People Team <people@northwind.example>
- **To:** All staff
- **Received:** Mon 5 Oct, 17:30
- **Subject:** Reminder: open enrolment closes 30 October

A reminder that open enrolment for benefits closes on 30 October. No action is needed if you're happy with your current choices.

---

## Email 12

- **From:** Webinar Hub <events@webinarhub.example>
- **To:** Sam Taylor
- **Received:** Mon 5 Oct, 23:00
- **Subject:** Last chance: register for "Future of Logistics" summit

Only 48 hours left to grab your early-bird ticket for the Future of Logistics summit.

[Register now] [Unsubscribe]

---

## Email 13

- **From:** Calendar <calendar@northwind.example>
- **To:** Sam Taylor
- **Received:** Tue 6 Oct, 07:00
- **Subject:** Accepted: Ops weekly sync (Thu 8 Oct, 09:00)

Lee Okafor has accepted your invitation: Ops weekly sync, Thursday 8 October, 09:00 to 09:30.

---

## Email 14

- **From:** Office Supplies Direct <offers@officesupplies.example>
- **To:** Sam Taylor
- **Received:** Tue 6 Oct, 05:30
- **Subject:** 20% off printer paper this week only

Stock up and save 20% on printer paper and toner until Sunday.

[Shop now] [Unsubscribe]

---

## Email 15

- **From:** Dana Whitfield <dana.whitfield@northwind.example>
- **To:** Ops Team
- **Received:** Mon 5 Oct, 18:40
- **Subject:** September KPI pack is on the shared drive

Hi all,

The September KPI pack is on the shared drive. On-time dispatch was 96.2%, up from 94.8% in August. No action needed; we'll go through it at Thursday's sync.

Dana
