"""Client for the /posts endpoints. Returns raw responses so tests can assert on status codes."""
import httpx

from api_tests.client import ApiClient


class PostsClient:
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def list(self, **filters) -> httpx.Response:
        return self._client.get("/posts", params=filters or None)

    def get(self, post_id) -> httpx.Response:
        return self._client.get(f"/posts/{post_id}")

    def comments(self, post_id) -> httpx.Response:
        return self._client.get(f"/posts/{post_id}/comments")

    def create(self, payload: dict) -> httpx.Response:
        return self._client.post("/posts", json=payload)

    def replace(self, post_id, payload: dict) -> httpx.Response:
        return self._client.put(f"/posts/{post_id}", json=payload)

    def update(self, post_id, payload: dict) -> httpx.Response:
        return self._client.patch(f"/posts/{post_id}", json=payload)

    def delete(self, post_id) -> httpx.Response:
        return self._client.delete(f"/posts/{post_id}")
