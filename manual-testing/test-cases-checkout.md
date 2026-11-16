# Test Cases: Checkout Flow

*Sample document on a fictional app (DemoShop).*

**Preconditions for all cases:** the app is installed, the user is logged in, the cart contains at least one available item, the internet connection is stable.

---

### TC-001: Successful checkout with a saved card

| Field | Value |
|-------|-------|
| **Priority** | Critical |
| **Type** | Smoke |
| **Steps** | 1. Open the cart<br>2. Tap **Checkout**<br>3. Select a delivery address<br>4. Select the saved card<br>5. Tap **Pay** |
| **Expected result** | The payment is accepted, the order confirmation screen shows the order number and the correct total, a confirmation notification arrives, the order appears in history with status "Paid" |

### TC-002: Remove an item from the cart

| Field | Value |
|-------|-------|
| **Priority** | High |
| **Type** | Smoke |
| **Steps** | 1. Add two items to the cart<br>2. Swipe one item to the left and tap **Delete** |
| **Expected result** | The item disappears and the cart total is recalculated immediately |

### TC-003: Change item quantity to the limit

| Field | Value |
|-------|-------|
| **Priority** | Medium |
| **Type** | Regression, boundary |
| **Steps** | 1. Add an item with a stock limit of 5<br>2. Increase quantity to 5<br>3. Try to increase to 6 |
| **Expected result** | The quantity stops at 5 and a clear message explains the limit. The total is correct |

### TC-004: Apply a valid promo code

| Field | Value |
|-------|-------|
| **Priority** | Medium |
| **Type** | Regression |
| **Steps** | 1. Open the cart<br>2. Enter `TEST2026`<br>3. Tap **Apply** |
| **Expected result** | The discount is shown as a separate line and the total is reduced. Applying the same code again does not stack the discount |

### TC-005: Apply an expired promo code

| Field | Value |
|-------|-------|
| **Priority** | Medium |
| **Type** | Negative |
| **Steps** | 1. Enter an expired code<br>2. Tap **Apply** |
| **Expected result** | A clear error message appears and the total does not change |

### TC-006: Payment with a declined card

| Field | Value |
|-------|-------|
| **Priority** | High |
| **Type** | Negative |
| **Steps** | 1. Select a test card that the bank declines<br>2. Tap **Pay** |
| **Expected result** | An error message is shown, no order is created, the user can choose another payment method |

### TC-007: Double tap on the Pay button

| Field | Value |
|-------|-------|
| **Priority** | High |
| **Type** | Edge case |
| **Steps** | 1. Open the payment screen<br>2. Tap **Pay** twice quickly |
| **Expected result** | Only one order and one charge are created. The button is disabled after the first tap |

### TC-008: Connection lost during payment

| Field | Value |
|-------|-------|
| **Priority** | Critical |
| **Type** | Network resilience |
| **Steps** | 1. Tap **Pay**<br>2. Turn off the internet for 2 seconds right after the tap<br>3. Turn it back on |
| **Expected result** | The payment is either completed once or clearly failed. The user is never charged twice. Order status and bank statement are consistent |
