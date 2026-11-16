# Regression Checklist: DemoShop (Pre-Release)

*Sample document on a fictional app.*

## 1. Authorization and profile
- [ ] Login by phone number (SMS code)
- [ ] Login with an invalid code shows an error
- [ ] Add and remove a delivery address
- [ ] Change the default payment method

## 2. Catalog and search
- [ ] Search by name returns relevant items
- [ ] Filters and sorting work together
- [ ] Item page shows price, availability and photos

## 3. Cart
- [ ] Add, remove and change quantity of items
- [ ] Cart total updates immediately after each change
- [ ] Out-of-stock item cannot be ordered
- [ ] Cart persists after the app restarts

## 4. Checkout and payments
- [ ] Payment with a saved card
- [ ] Payment with Apple Pay / Google Pay
- [ ] Cash on delivery
- [ ] Promo code: valid, expired, already used
- [ ] Declined card shows an error and creates no order
- [ ] Double tap on **Pay** creates only one order

## 5. Orders and notifications
- [ ] New order appears in history with the correct total
- [ ] Order status updates (paid, packed, shipped, delivered)
- [ ] Order cancellation before shipping
- [ ] Push notification arrives for each status change

## 6. Background and network
- [ ] App does not crash when minimized during checkout
- [ ] Internet loss for 10 seconds does not duplicate an order
- [ ] Order status refreshes after the connection returns
- [ ] Screen rotation does not lose the cart or checkout data
