"""Thin HTTP wrapper: logs every call and attaches request and response to the Allure report."""
import logging

import allure
import httpx

logger = logging.getLogger("api_tests")
MAX_ATTACHMENT_CHARS = 5000


class ApiClient:
    def __init__(self, base_url: str, timeout: float = 15.0) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={"Accept": "application/json"},
        )

    def request(self, method: str, path: str, **kwargs) -> httpx.Response:
        with allure.step(f"{method} {path}"):
            response = self._client.request(method, path, **kwargs)
            logger.info("%s %s -> %s", method, path, response.status_code)
            self._attach(response)
            return response

    def get(self, path: str, **kwargs) -> httpx.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> httpx.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> httpx.Response:
        return self.request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs) -> httpx.Response:
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs) -> httpx.Response:
        return self.request("DELETE", path, **kwargs)

    def close(self) -> None:
        self._client.close()

    @staticmethod
    def _attach(response: httpx.Response) -> None:
        request = response.request
        request_text = f"{request.method} {request.url}\n\n{request.content.decode(errors='replace')}"
        response_text = f"{response.status_code}\n\n{response.text}"
        allure.attach(
            request_text[:MAX_ATTACHMENT_CHARS],
            name="request",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            response_text[:MAX_ATTACHMENT_CHARS],
            name="response",
            attachment_type=allure.attachment_type.TEXT,
        )
