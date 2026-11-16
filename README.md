# QA Portfolio | Daniil Chaykin

Fullstack QA Engineer with 5+ years of experience in full-cycle testing: manual testing of web and mobile apps (iOS, Android), API test automation in Python, SQL data checks, CI and reporting.

> **About the examples.** Everything in this repository is a demonstration built on a fictional shopping app ("DemoShop") and a public demo API. It contains no data, screenshots, code or internal details from any employer or client.

## What is inside

| Folder | Contents |
|--------|----------|
| [`manual-testing/`](manual-testing) | Test plan, test cases, regression checklist and five bug reports |
| [`api-automation/`](api-automation) | Runnable Python API test framework: pytest, httpx, pydantic, Allure, CI |
| [`sql/`](sql) | SQL queries for data integrity checks: duplicates, payment mismatches, stuck orders |
| [`projects/`](projects) | Write-ups of larger automation work: API framework approach and an MCP server for QA tooling |

## Skills

- **Manual testing:** functional, regression, exploratory, cross-platform, test design (test cases, checklists, test plans)
- **API testing and automation:** Python, pytest, httpx, pydantic, Postman, OpenAPI contract checks
- **UI automation:** Playwright, Selenium, Appium
- **CI/CD and reporting:** GitHub Actions, GitLab CI, Allure Report, Allure TestOps
- **Debugging tools:** Charles Proxy, DevTools, Android Studio, Xcode, mobile and microservice logs
- **Databases:** PostgreSQL, MySQL, DataGrip
- **Bug tracking and docs:** Jira, Confluence, YouTrack
- **AI in QA:** LLM-assisted test design, MCP servers for test management

## Quick start (API automation demo)

```bash
cd api-automation
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Reports with Allure:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Contact

- Email: daneelchaykin@gmail.com
- LinkedIn: [linkedin.com/in/daniil-chaykin](https://www.linkedin.com/in/daniil-chaykin)
- Telegram: [@DanSeagull](https://t.me/DanSeagull)
- GitHub: [github.com/DanSeagull](https://github.com/DanSeagull)
