import pytest

from api_tests.client import ApiClient
from api_tests.config import settings
from api_tests.services.posts import PostsClient
from api_tests.services.users import UsersClient


@pytest.fixture(scope="session")
def api_client():
    client = ApiClient(settings.base_url, settings.timeout)
    yield client
    client.close()


@pytest.fixture(scope="session")
def posts(api_client):
    return PostsClient(api_client)


@pytest.fixture(scope="session")
def users(api_client):
    return UsersClient(api_client)


@pytest.fixture
def new_post_payload():
    return {
        "title": "QA sample post",
        "body": "Created by an automated test",
        "userId": 1,
    }
