# DS-1051: Double charge after a short network loss during payment

| Field | Value |
|-------|-------|
| **Severity** | Critical (financial risk) |
| **Priority** | Blocker |
| **Status** | New |
| **Reproducibility** | 4 of 5 |
| **Build** | DemoShop 3.8.1 (412), staging |
| **Device** | Samsung S22, Android 13 |

## Preconditions
User is logged in with a saved test card. The cart contains items worth $25.

## Steps to reproduce
1. Go to **Checkout** and tap **Pay**.
2. Right after the tap, turn off Wi-Fi and mobile data for 1-2 seconds.
3. Turn the connection back on.
4. Check the order history and the test card transactions.

## Expected result
The retried request does not create a second transaction (idempotent payment API). One order, one charge.

## Actual result
Two charges of $25 appear on the test card. Order history shows a single order. The backend treated the retried request as a new payment.

## Technical details
```
POST /payments   -> (connection lost, no response received)
POST /payments   -> 201 Created   // client retry, no Idempotency-Key header
```
The same request body was sent twice without an idempotency key, so the server created two payments.

## Impact
Direct financial loss for customers, chargebacks and support load. Blocks the release.

## Suggested fix
Send an `Idempotency-Key` header generated once per payment attempt and reject duplicates on the server.

## Attachments
Screen recording, network log with both requests (not included in this sample).
