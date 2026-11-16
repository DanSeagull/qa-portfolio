# DS-1063: `POST /orders` returns 500 when the comment contains an emoji

| Field | Value |
|-------|-------|
| **Severity** | Minor |
| **Priority** | Low |
| **Status** | New |
| **Reproducibility** | 5 of 5 |
| **Environment** | Staging API v2, Postman |

## Steps to reproduce
1. Send `POST /orders` with a valid body.
2. Add an emoji to the `comment` field, as in the request below.
3. Send the request.

## Request
```json
{
  "items": [{"sku": "A-100", "qty": 1}],
  "address_id": 17,
  "comment": "Please leave at the door 🚪"
}
```

## Expected result
`201 Created`. The emoji is saved or safely replaced. If the value is not allowed, the API returns `400` with a clear validation error.

## Actual result
`500 Internal Server Error` with an empty error body. The order is not created.

## Notes
Plain text comments work. Likely cause: database column encoding does not support 4-byte Unicode characters (hypothesis, to be confirmed by the backend team). The same problem may affect other free-text fields (profile name, address notes).

## Attachments
Postman request and response export (not included in this sample).
