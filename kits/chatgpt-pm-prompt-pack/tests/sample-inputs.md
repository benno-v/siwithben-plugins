# Sample inputs for testing

*By Benjamin Vermeulen, SI with Ben (@SIwithBen)*

These are the same five scenarios I use in my videos. All companies, figures and details are fictional. Paste each one into the GPT (or the matching prompt in `prompt-pack.md`) and check the result against the "What to check" list.

---

## Test 1: Project Charter

```
Create a project charter for "Project Atlas", a redesign of our e-commerce website.
We sell home and kitchen products online across the EU. The current site is slow on mobile and conversion has dropped, so we want a full redesign of the storefront and checkout within 3 months. The site must stay GDPR compliant, including cookie consent and customer data handling.
```

What to check:
- Under 2 pages, bullets throughout, all ten sections in order.
- SMART objectives have a measure and a date; missing targets are marked "TBC", not invented.
- Budget and sponsor show "Not provided" (or the GPT asks once for them).
- GDPR appears as a constraint and the Data Protection Officer (or similar role) as a stakeholder.

---

## Test 2: WBS and PERT estimation

```
Break down this requirement into a WBS with three-point estimates:
Build a fitness tracking mobile app using React Native and Firebase. Users can sign up and log in, log workouts (type, duration, notes), see a weekly progress chart, and receive a push notification reminder if they haven't logged a workout in 3 days. Team: 2 developers, 1 designer, 1 QA.
```

What to check:
- Indented WBS with numbered levels, including testing, deployment and project management.
- Every task has O, M, P, E and SD, with O <= M <= P.
- E = (O + 4M + P) / 6 and SD = (P - O) / 6 are correct for a few spot-checked rows.
- Totals, confidence range (E plus or minus 2 SD) and the effort-by-role table are present.

---

## Test 3: Risk register

```
Identify the top 10 risks for a marketing campaign project in sustainable fashion.
Project specifics: launch campaign for a sustainable fashion brand targeting Gen Z. Budget USD 300,000 over six months. Channels: Instagram, TikTok, influencer partnerships, email and SEO.
```

What to check:
- 10 risks across technical, external, organisational and project management categories.
- Probability and impact are H/M/L; scores are probability x impact using H = 3, M = 2, L = 1; sorted highest first.
- Specific risks (for example influencer greenwashing claims, platform algorithm changes), not generic ones.
- Owners are roles. The table pastes cleanly into Excel.
- Follow-up: ask for 40 risks and check that the GPT warns about quality before proceeding.

---

## Test 4: Executive translator

```
Translate this technical update into an executive summary for our sponsor:
The admin panel went down on Tuesday for about 6 hours after a database migration locked the orders table. We rolled back and the panel is up, but the migration still needs to run. Root cause is that our ORM generates inefficient queries on large tables and the team doesn't have deep database tuning experience. We recommend bringing in a specialist database consultant for 3 weeks at USD 12,000 to fix the queries and re-run the migration safely. Without this, the planned reporting feature will slip by about a month.
```

What to check:
- 3 to 5 bullets, no jargon such as "ORM" left unexplained.
- Timeline (about one month slip) and budget (USD 12,000) both appear, with no extra figures invented.
- Exactly one decision: approve the USD 12,000 consultant or accept the delay.

---

## Test 5: Weekly status report

```
Generate my weekly status report.
Project: Customer Portal Upgrade
Week ending: 9 Oct 2026
Tasks completed: login redesign signed off; API for order history deployed to test
Tasks in progress: payment page integration (about 60% done); accessibility review
Blockers: still waiting on the payment provider's sandbox credentials, requested two weeks ago
Upcoming milestones: user acceptance testing starts 23 Oct 2026; go-live 13 Nov 2026
Budget status: 62% spent
Schedule status: At risk
```

What to check:
- RAG is Amber (or Red with a clear reason), with a one-line reason linked to the payment sandbox blocker.
- Blocker table shows the impact on user acceptance testing and who needs to act.
- Budget shows 62% spent and "Comparison to plan: Not provided"; no SPI or CPI calculated.
- Follow-up: add "PV USD 100,000, EV USD 90,000, AC USD 110,000" and check that SPI = 0.90 and CPI = 0.82 appear with formulas.
