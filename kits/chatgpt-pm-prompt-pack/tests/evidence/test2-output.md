Reminder: do not paste confidential client or personal data unless your workspace policy allows it. Anonymise names and figures if unsure.

# WBS and Estimates: Fitness Tracking Mobile App

**Basis:** React Native and Firebase mobile app with sign-up and login, workout logging (type, duration, notes), a weekly progress chart and a push reminder after 3 days without a logged workout.
**Units:** effort hours. Estimates are planning estimates for the team to validate.

## 1. Work breakdown structure
- 1 Project management and setup
  - 1.1 Project management
    - 1.1.1 Sprint planning, backlog and coordination
    - 1.1.2 Stakeholder reviews and user acceptance testing (UAT) coordination
  - 1.2 Technical setup
    - 1.2.1 Repository, React Native project and CI pipeline set-up
    - 1.2.2 Firebase project configuration (Auth, Firestore, Cloud Messaging, environments)
- 2 Design
  - 2.1 UX and UI
    - 2.1.1 User flows and wireframes
    - 2.1.2 Visual design system and component styles
    - 2.1.3 High-fidelity screens (auth, workout log, history, progress, settings)
    - 2.1.4 Design handover and review with developers
- 3 Authentication
  - 3.1 Sign-up and login
    - 3.1.1 Sign-up and login screens with validation
    - 3.1.2 Firebase Auth integration (sign-up, login, logout, session persistence)
- 4 Workout logging
  - 4.1 Log and view workouts
    - 4.1.1 Firestore data model and security rules for workouts
    - 4.1.2 Log workout form (type, duration, notes) with validation
    - 4.1.3 Workout history list with edit and delete
- 5 Progress chart
  - 5.1 Weekly progress
    - 5.1.1 Weekly aggregation logic
    - 5.1.2 Chart component and progress screen
- 6 Push notification reminder
  - 6.1 Inactivity reminder
    - 6.1.1 Firebase Cloud Messaging set-up for iOS and Android
    - 6.1.2 Scheduled Cloud Function to detect 3 days without a workout and send reminder
    - 6.1.3 In-app notification handling and opt-out setting
- 7 Testing and quality
  - 7.1 Quality assurance
    - 7.1.1 Test plan and test cases
    - 7.1.2 Functional testing on iOS and Android devices
    - 7.1.3 Notification and edge-case testing
    - 7.1.4 Regression testing and bug verification
  - 7.2 Development quality
    - 7.2.1 Bug fixing
    - 7.2.2 Unit tests for core logic
- 8 Deployment
  - 8.1 Release
    - 8.1.1 App store assets (icon, screenshots)
    - 8.1.2 Build, signing and submission to App Store and Google Play
    - 8.1.3 Production release checks and monitoring set-up

## 2. Task estimates
| ID | Task | Hours (O) | Hours (M) | Hours (P) | Hours (E) | SD | Depends on | Skills / role | Key risk |
|---|---|---|---|---|---|---|---|---|---|
| 1.1.1 | Sprint planning, backlog and coordination | 16.0 | 25.0 | 40.0 | 26.0 | 4.0 | None | Project Manager | Scope changes increase coordination effort |
| 1.1.2 | Stakeholder reviews and UAT coordination | 8.0 | 11.0 | 20.0 | 12.0 | 2.0 | 1.1.1 | Project Manager | Late stakeholder feedback |
| 1.2.1 | Repository, React Native project and CI set-up | 8.0 | 11.0 | 20.0 | 12.0 | 2.0 | None | Developer | iOS build tooling issues |
| 1.2.2 | Firebase project configuration | 4.0 | 7.0 | 16.0 | 8.0 | 2.0 | 1.2.1 | Developer | Environment separation not agreed |
| 2.1.1 | User flows and wireframes | 12.0 | 18.0 | 30.0 | 19.0 | 3.0 | None | Designer | Unclear requirements for history and settings |
| 2.1.2 | Visual design system and component styles | 18.0 | 24.0 | 36.0 | 25.0 | 3.0 | 2.1.1 | Designer | No existing brand guidelines |
| 2.1.3 | High-fidelity screens | 16.0 | 22.0 | 34.0 | 23.0 | 3.0 | 2.1.2 | Designer | Multiple design review rounds |
| 2.1.4 | Design handover and review with developers | 4.0 | 7.0 | 10.0 | 7.0 | 1.0 | 2.1.3 | Designer | Designs not feasible in React Native |
| 3.1.1 | Sign-up and login screens with validation | 10.0 | 16.0 | 28.0 | 17.0 | 3.0 | 1.2.1; 2.1.4 | Developer | Error state handling underestimated |
| 3.1.2 | Firebase Auth integration | 8.0 | 14.0 | 26.0 | 15.0 | 3.0 | 1.2.2 | Developer | Session persistence edge cases |
| 4.1.1 | Firestore data model and security rules | 6.0 | 9.0 | 18.0 | 10.0 | 2.0 | 1.2.2 | Developer | Weak security rules expose user data |
| 4.1.2 | Log workout form with validation | 8.0 | 11.0 | 20.0 | 12.0 | 2.0 | 4.1.1; 2.1.4 | Developer | Workout type list not defined |
| 4.1.3 | Workout history list with edit and delete | 10.0 | 16.0 | 28.0 | 17.0 | 3.0 | 4.1.2 | Developer | Edit and delete scope not confirmed |
| 5.1.1 | Weekly aggregation logic | 6.0 | 9.0 | 18.0 | 10.0 | 2.0 | 4.1.1 | Developer | Week start and time zone rules unclear |
| 5.1.2 | Chart component and progress screen | 12.0 | 18.0 | 30.0 | 19.0 | 3.0 | 5.1.1; 2.1.4 | Developer | Chart library limits on styling |
| 6.1.1 | Cloud Messaging set-up for iOS and Android | 8.0 | 14.0 | 26.0 | 15.0 | 3.0 | 1.2.2 | Developer | Apple push certificate and permission issues |
| 6.1.2 | Scheduled function for 3-day inactivity reminder | 10.0 | 16.0 | 34.0 | 18.0 | 4.0 | 6.1.1; 4.1.1 | Developer | Time zone logic causes wrong send times |
| 6.1.3 | In-app notification handling and opt-out | 6.0 | 9.0 | 18.0 | 10.0 | 2.0 | 6.1.1 | Developer | Behaviour differs between iOS and Android |
| 7.1.1 | Test plan and test cases | 8.0 | 11.0 | 20.0 | 12.0 | 2.0 | 2.1.1 | QA | Acceptance criteria not defined |
| 7.1.2 | Functional testing on iOS and Android | 16.0 | 25.0 | 40.0 | 26.0 | 4.0 | 3.1.2; 4.1.3; 5.1.2; 6.1.3 | QA | Limited range of test devices |
| 7.1.3 | Notification and edge-case testing | 6.0 | 9.0 | 18.0 | 10.0 | 2.0 | 6.1.2 | QA | 3-day trigger hard to simulate |
| 7.1.4 | Regression testing and bug verification | 8.0 | 14.0 | 26.0 | 15.0 | 3.0 | 7.2.1 | QA | High defect count extends cycles |
| 7.2.1 | Bug fixing | 16.0 | 25.0 | 40.0 | 26.0 | 4.0 | 7.1.2 | Developer | Defect volume unknown at this stage |
| 7.2.2 | Unit tests for core logic | 8.0 | 11.0 | 20.0 | 12.0 | 2.0 | 5.1.1; 6.1.2 | Developer | Firebase services hard to mock |
| 8.1.1 | App store assets | 4.0 | 7.0 | 10.0 | 7.0 | 1.0 | 2.1.3 | Designer | Store size requirements missed |
| 8.1.2 | Build, signing and store submission | 6.0 | 9.0 | 18.0 | 10.0 | 2.0 | 7.1.4; 8.1.1 | Developer | App store review rejection |
| 8.1.3 | Production release checks and monitoring set-up | 4.0 | 7.0 | 10.0 | 7.0 | 1.0 | 8.1.2 | Developer | Production config differs from test |

## 3. Summary
- Formula: E = (O + 4M + P) / 6; SD = (P - O) / 6
- Total expected effort (E): 400.0 hours
- Total SD: square root of (sum of SD squared) = square root of 192.0 = 13.9 hours
- Sum of SD squared: (4 tasks x 16) + (9 tasks x 9) + (11 tasks x 4) + (3 tasks x 1) = 64 + 81 + 44 + 3 = 192
- Confidence range (E plus or minus 2 SD): 372.3 to 427.7 hours
- Number of tasks: 27

## 4. Effort by role
| Role | Tasks | Hours (E) | Share of total |
|---|---|---|---|
| Developer | 16 | 218.0 | 54.5% |
| Designer | 5 | 81.0 | 20.3% |
| QA | 4 | 63.0 | 15.8% |
| Project Manager | 2 | 38.0 | 9.5% |
| Total | 27 | 400.0 | 100% |

## 5. Assumptions and notes
- These are planning estimates for the team to validate. Hours are effort, not elapsed calendar time.
- Developer effort (218.0 hours) is shared by 2 developers. Calendar duration depends on how work is split and run in parallel.
- Shares of total are rounded to one decimal place, so they add up to 100.1%.
- A Project Manager role is assumed. It was not in the team you listed. Please confirm who covers this work (needs validating).
- Both iOS and Android are assumed to be in scope (needs validating).
- Edit and delete in workout history and an opt-out setting for notifications are assumed. They were not in the requirement (needs validating).
- Out of scope unless confirmed: password reset, social login, offline mode, admin panel, analytics and Apple Health or Google Fit integration.
- The "3 days" rule is assumed to count from the last logged workout in the user's local time zone. The rule for the start of the week on the chart is TBC.
- App Store and Google Play developer accounts are assumed to exist already (needs validating).
- Deadline: Not provided.
- Workout data may be treated as health data under data protection law. The Data Protection Officer should confirm any obligations before release.

Review before sharing: this is an AI draft and you are the final quality gate for accuracy, numbers and tone.

**Next steps:** I can:
- Adjust the estimates or level of detail for a specific phase, such as notifications or testing.
- Convert the task table to CSV or an Excel file.
- Build a risk register for this app using the risk template.
