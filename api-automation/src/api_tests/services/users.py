"""Client for the /users endpoints."""
import httpx

from api_tests.client import ApiClient


class UsersClient:
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def list(self) -> httpx.Response:
        return self._client.get("/users")

    def get(self, user_id) -> httpx.Response:
        return self._client.get(f"/users/{user_id}")
