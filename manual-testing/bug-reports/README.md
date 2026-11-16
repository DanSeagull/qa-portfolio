# Bug Reports (samples)

Five reports on a fictional app (DemoShop), covering different severities and layers: payments, API, UI, device behavior and stability. In real projects every report also carries a screen recording, screenshots and a network or device log.

| ID | Title | Severity | Layer |
|----|-------|----------|-------|
| [DS-1042](DS-1042-cart-total-not-updated.md) | Cart total not updated after removing an item (iOS) | Major | UI / API cache |
| [DS-1051](DS-1051-double-charge-network-loss.md) | Double charge after a short network loss during payment | Critical | Payments / API |
| [DS-1063](DS-1063-api-500-emoji-comment.md) | `POST /orders` returns 500 when the comment contains an emoji | Minor | API |
| [DS-1077](DS-1077-crash-fast-scroll-history.md) | App crashes on fast scrolling of a long order history | Major | Stability |
| [DS-1088](DS-1088-address-autodetect-low-power.md) | Delivery address auto-detect is 600 m off in Low Power Mode | Normal | Device / location |
