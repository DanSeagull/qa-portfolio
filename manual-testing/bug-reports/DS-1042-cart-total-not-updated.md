# DS-1042: Cart total not updated after removing an item (iOS)

| Field | Value |
|-------|-------|
| **Severity** | Major |
| **Priority** | High |
| **Status** | New |
| **Reproducibility** | 5 of 5 |
| **Build** | DemoShop 3.8.1 (412), staging |
| **Device** | iPhone 14, iOS 17.4, Wi-Fi |
| **Not reproduced on** | Android 14 |

## Preconditions
User is logged in. The cart contains Item A ($20) and Item B ($35).

## Steps to reproduce
1. Open the **Cart** screen. The total shows $55.
2. Swipe Item B to the left and tap **Delete**.
3. Look at the **Total** value.

## Expected result
Item B is removed and the total updates to $20 immediately.

## Actual result
Item B is removed, but the total still shows $55 until the screen is reopened. Checkout then charges $55.

## Technical details
```
DELETE /cart/items/42   -> 200 OK
GET    /cart            -> 200 OK   {"items": 1, "total": 55}   // stale, expected 20
```
Possible cause (hypothesis): the cart response is cached on the client after the delete request.

## Impact
Users can be overcharged at checkout: risk of refunds and complaints.

## Attachments
Screen recording (12 s), 3 screenshots, network log (not included in this sample).
