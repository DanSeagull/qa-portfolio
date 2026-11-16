# API Test Automation Framework

A production-grade API test automation framework that I design and build: typed service clients, CI, live reporting, contract validation, real-time checks and production synthetic monitoring.

> Generalized write-up of my approach and skills. No employer-specific architecture, business logic, internal tooling, credentials or metrics are included.

## Stack

`Python` · `pytest` · `httpx` · `pydantic` · `allure-pytest` · `websockets` · `GitHub Actions` · `Allure Report` · `Allure TestOps` · `jsonschema`

## What I build

- **Functional and negative API coverage** for a set of microservices behind a token-based auth gateway: authentication and session lifecycle, user data, files, billing and an asynchronous job pipeline.
- Assertions target a **stable machine-readable error contract** (`errorCode`), not brittle message text, so tests survive copy changes.
- **Typed client layer** (`src/` layout, one client per service over a thin `httpx` wrapper): auth headers, request and response logging into the report. Tests receive ready sessions from fixtures instead of assembling tokens by hand.

## Highlights

- **Monetization testing without real payments:** the suite simulates payment provider webhooks with correctly signed requests, then verifies balances and subscription state: grants, idempotency on retries, out-of-order events, cancellation, balance invariants.
- **Real-time checks:** subscribes to the WebSocket channel used for live updates and validates the pushed events.
- **Concurrency and rate-limit tests:** parallel request bursts prove that server-side limits hold under simultaneous calls, not only sequential ones.
- **Storage tests:** file classes, per-user listing with pagination, usage accounting based on the real uploaded size, isolation between users.
- **Environment guard:** mutating suites refuse to run against production, and every test creates and cleans up its own users and data.
- **Production synthetic monitoring:** a separate zero-mutation smoke suite (availability, auth gateway, latency thresholds) plus a read-only authenticated tier on a dedicated test account, built to stay within production rate limits.
- **Live email-flow automation:** end-to-end password recovery driven by reading a one-time code from a test inbox over IMAP.
- **OpenAPI contract-drift detection:** responses are validated against service OpenAPI specs (`jsonschema`). A spec violation fails the test as contract drift.
- **Known issues as code:** confirmed bugs stay in the suite as expected failures with a clear reason and turn green on their own once fixed.
- **Live reporting and feedback:** Allure HTML on GitHub Pages with trend history per environment, results in Allure TestOps, nightly runs posting summaries to a team chat.

## How I use it in a team

- **Pre-release verification of backend tasks:** I read the task, turn the acceptance criteria into automated checks on the test environment, and report what is covered automatically and what needs a manual check.
- **Bug investigation:** reproducing client-reported issues through the API and analyzing mobile diagnostic logs to separate client bugs from backend ones.
- The suite surfaces real defects before release.

## Engineering practices

- Every external integration is **gated behind secrets and degrades softly**: a missing secret skips that step instead of breaking CI.
- Production checks are **non-destructive by design**. Anything that could create data is isolated to the test environment.
- Tests stay quiet for the backend: no stray errors or alerts caused by test traffic.

## My role

Designed and built the framework end to end: architecture, test suites, CI/CD, reporting, production monitoring and the reporting and notification automations.

## See it in code

A compact runnable example of the same ideas (typed clients, pydantic models, contract checks, known issues as code, CI) is in [`../api-automation`](../api-automation).
