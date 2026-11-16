# DS-1088: Delivery address auto-detect is 600 m off in Low Power Mode

| Field | Value |
|-------|-------|
| **Severity** | Normal |
| **Priority** | Medium |
| **Status** | New |
| **Reproducibility** | 5 of 5 in Low Power Mode, 0 of 5 without it |
| **Build** | DemoShop 3.8.1 (412), staging |
| **Device** | iPhone 15, iOS 17.2 |
| **Location** | Dense city center with high-rise buildings |

## Steps to reproduce
1. Enable **Low Power Mode** on the device.
2. Stand near high-rise buildings with a clear outdoor view.
3. Open **Checkout** and tap **Use current location** for the delivery address.
4. Compare the suggested address with the real one.

## Expected result
The suggested address matches the real position, or the app asks the user to confirm or enter the address manually when accuracy is low.

## Actual result
The app suggests an address from the neighboring block, about 600 m away, without any warning. With Low Power Mode off, the address is correct.

## Technical details
```
[Location] didUpdateLocations: accuracy = 245 m   (expected < 100 m)
[Location] first fix delay: 8 s
```

## Impact
Orders can be delivered to the wrong address if the user does not notice the mistake.

## Suggested fix
Ignore location fixes with low accuracy and show a confirmation step when accuracy is above the threshold.

## Attachments
Screen recording and device log (not included in this sample).
