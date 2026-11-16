# DS-1077: App crashes on fast scrolling of a long order history

| Field | Value |
|-------|-------|
| **Severity** | Major |
| **Priority** | High |
| **Status** | New |
| **Reproducibility** | 5 of 5 |
| **Build** | DemoShop 3.8.1 (412), production-like |
| **Device** | iPhone 11, iOS 17.2 (4 GB RAM) |
| **Test data** | Account with 50+ orders |

## Steps to reproduce
1. Open **My orders** and then **History**.
2. Scroll the list quickly up and down 5-6 times.

## Expected result
Scrolling is smooth and the app stays stable.

## Actual result
The app closes and returns to the home screen. The crash report shows an out-of-memory termination: all order preview images are loaded into memory at once.

## Impact
Users with a long purchase history lose access to their orders and may leave the app.

## Notes
Does not reproduce on accounts with fewer than 20 orders. Suggested fix: lazy loading with image caching and pagination.

## Attachments
Screen recording, crash report (not included in this sample).
