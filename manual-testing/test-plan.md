# Test Plan: DemoShop Mobile App (Customer Version)

*Sample document on a fictional app.*

## 1. Test Object

**Product:** DemoShop, a shopping app: catalog, cart, checkout, order tracking.

**Platforms:** iOS (last 2 major versions), Android (last 3 major versions), mobile web.

**In scope**
- **Core flow:** search or browse, add to cart, checkout, payment, order confirmation
- **Payments:** card, Apple Pay / Google Pay, cash on delivery, promo codes
- **Orders:** order history, status updates, cancellation, push notifications
- **Profile:** registration, login (SMS code), addresses, payment methods

**Out of scope:** backend load testing, dark mode, admin panel, courier app.

## 2. Types of Testing

| Type | Why it matters | Tools |
|------|----------------|-------|
| Functional | A user must complete an order without failures | Manual, checklists |
| Integration | The app depends on a payment gateway, an SMS provider and a maps service | Charles Proxy, Postman |
| API | Most business logic lives on the backend, and defects are found earlier there | Postman, pytest |
| Data integrity | Orders and payments must always match | SQL (DataGrip) |
| UI / UX | Layouts, rotation, small screens, accessibility basics | Figma, DevTools, Xcode, Android Studio |
| Network resilience | Weak or lost connection during payment | Network Link Conditioner, Charles throttling |
| Cross-platform | Different navigation behavior on iOS and Android | Real devices, simulators |
| Regression | Each release must not break checkout or payments | Checklist, automated API suite |

## 3. Approach

**Manual**
- **Exploratory:** real purchase scenarios with different carts, addresses and payment methods
- **Negative:** empty fields, invalid cards, expired promo codes, no internet, repeated taps
- **Cross-device:** small screens, tablets, different OS versions

**Emulation tools**
- **Charles Proxy:** mock server responses (for example, empty catalog or payment timeout)
- **Xcode / Android Studio:** simulate poor network, location and low memory
- **Postman:** direct API checks, including data that the UI does not allow to enter

## 4. Exit Criteria

Testing is complete when:
1. There are no open **blocker or critical** defects in checkout and payments.
2. All **smoke and high-priority regression** cases pass on both platforms.
3. No crashes in the crash-reporting tool during a 10-minute background and foreground session.
4. Payment and order amounts match in the database for all test purchases.

## 5. Resources and Test Data

**Devices:** iPhone 15 (iOS 17), iPhone SE simulator (small screen), Pixel 6 (Android 14), Samsung S22 (Android 13).

**Accounts**
- User with a saved card (3-D Secure and non-3-D Secure)
- User with an empty order history
- User with an active promo code (`TEST2026`) and one with an expired code
- User with a blocked payment method

## 6. Risks

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Incorrect charges or double charges | Medium | API and database checks of every payment scenario, network-loss tests |
| Cart and total out of sync | Medium | Automated API assertions after every cart change |
| Device fragmentation on Android | High | Cover the lowest and the highest supported versions, test on real devices |
| Third-party outages (payments, SMS) | Low | Mock responses, verify error messages and retry behavior |

## 7. Schedule (example for one sprint)

| Day | Activity |
|-----|----------|
| 1 | Requirements review, test design, checklists |
| 2 | Functional testing, bug reporting |
| 3 | API and integration testing |
| 4 | Regression and retest of fixes |
| 5 | Final report, release recommendation |

## 8. Deliverables

Test cases, regression checklist, bug reports with evidence, final test summary.
