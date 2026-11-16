-- Data integrity checks for the DemoShop sample schema (PostgreSQL).
--
-- users(user_id, phone, email, created_at)
-- orders(order_id, user_id, status, total_amount, created_at)
-- payments(payment_id, order_id, amount, status, created_at)


-- 1. Possible duplicate orders: same user, same total, created within one minute.
--    Use after testing double taps and network loss during checkout.
SELECT
    o1.user_id,
    o1.order_id AS first_order,
    o2.order_id AS second_order,
    o1.total_amount,
    o2.created_at - o1.created_at AS time_gap
FROM orders o1
JOIN orders o2
  ON o1.user_id = o2.user_id
 AND o1.total_amount = o2.total_amount
 AND o2.order_id > o1.order_id
 AND o2.created_at - o1.created_at < INTERVAL '1 minute'
WHERE o1.created_at > NOW() - INTERVAL '1 hour'
ORDER BY o1.created_at DESC;


-- 2. Orders whose payment amount differs from the order total.
SELECT
    o.order_id,
    o.total_amount,
    p.amount AS payment_amount,
    ABS(o.total_amount - p.amount) AS difference
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE p.status = 'completed'
  AND ABS(o.total_amount - p.amount) > 0.01;


-- 3. Double charges: more than one completed payment for the same order.
SELECT
    order_id,
    COUNT(*) AS completed_payments,
    SUM(amount) AS total_charged
FROM payments
WHERE status = 'completed'
GROUP BY order_id
HAVING COUNT(*) > 1;


-- 4. Orders without a completed payment although they are marked as paid.
SELECT o.order_id, o.status, o.total_amount, o.created_at
FROM orders o
LEFT JOIN payments p
  ON p.order_id = o.order_id AND p.status = 'completed'
WHERE o.status = 'paid'
  AND p.payment_id IS NULL;


-- 5. Stuck orders: still in processing after 4 hours.
SELECT
    order_id,
    status,
    created_at,
    NOW() - created_at AS age
FROM orders
WHERE status = 'processing'
  AND created_at < NOW() - INTERVAL '4 hours'
ORDER BY created_at;


-- 6. Test data: create a test user (staging only).
INSERT INTO users (phone, email, created_at)
VALUES ('+10000000001', 'qa.user@example.com', NOW())
ON CONFLICT (phone) DO NOTHING;


-- 7. Test data cleanup: remove orders and payments created by the test user (staging only).
DELETE FROM payments
WHERE order_id IN (
    SELECT order_id FROM orders
    WHERE user_id IN (SELECT user_id FROM users WHERE email = 'qa.user@example.com')
);

DELETE FROM orders
WHERE user_id IN (SELECT user_id FROM users WHERE email = 'qa.user@example.com');
