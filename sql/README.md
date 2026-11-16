# SQL Data Integrity Checks

Queries I use to verify what the UI and the API cannot prove on their own. They are written for a fictional schema (PostgreSQL syntax) used in the DemoShop samples.

```
users(user_id, phone, email, created_at)
orders(order_id, user_id, status, total_amount, created_at)
payments(payment_id, order_id, amount, status, created_at)
```

| File | Purpose |
|------|---------|
| [`data-integrity-checks.sql`](data-integrity-checks.sql) | Duplicate orders, order and payment mismatches, double charges, stuck orders, test data setup and cleanup |
