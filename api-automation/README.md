# API Test Automation Demo

A compact, runnable example of how I structure API test automation: typed clients, pydantic models, contract checks, known issues kept as code, Allure reporting and CI.

It runs against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a free public fake REST API, so it works without credentials. To use the same structure on a real project, set `BASE_URL` and replace the clients and models.

## Stack

`Python` · `pytest` · `httpx` · `pydantic` · `allure-pytest` · `GitHub Actions`

## Run

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest                      # everything
pytest -m smoke             # fast checks only
pytest -m "not contract"    # skip contract checks
```

Allure report:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

Use another API: `BASE_URL=https://example.com pytest`

## Structure

```
api-automation/
├── src/api_tests/
│   ├── client.py        # httpx wrapper: logging and Allure attachments
│   ├── config.py        # settings from environment variables
│   ├── models.py        # pydantic models (contract)
│   └── services/        # one client per service area
├── tests/
│   ├── test_posts_read.py
│   ├── test_posts_write.py
│   ├── test_users.py
│   ├── test_negative.py
│   └── test_contract.py
├── conftest.py          # shared fixtures
└── pytest.ini           # markers: smoke, regression, negative, contract
```

## Design notes

- **Typed clients:** tests call `posts.get(1)`, not raw URLs. A change in a path is fixed in one place.
- **Contract through models:** pydantic models use `extra="forbid"`, so a new or missing field fails the test as contract drift.
- **Known issues as code:** `test_created_post_can_be_read_back` is marked `xfail` with a reason. It documents a known limitation of the demo API and turns into an unexpected pass on its own once the behavior changes.
- **Readable failures:** every request and response is attached to the Allure report.
- **Markers:** `smoke` for a quick gate, `regression` for full coverage, `negative` and `contract` for focused runs.
- **CI:** GitHub Actions runs the suite on every push, on pull requests and nightly, and stores Allure results as an artifact (see `.github/workflows/api-tests.yml` at the repository root).

## Note about the demo API

JSONPlaceholder accepts writes (`POST`, `PUT`, `PATCH`, `DELETE`) and returns realistic responses, but it does not save anything. That is why the tests check the response of each write and not the stored state.
