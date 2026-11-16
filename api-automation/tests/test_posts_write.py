import pytest

from api_tests.models import Post

pytestmark = pytest.mark.regression


@pytest.mark.smoke
def test_create_post_returns_201_and_echoes_payload(posts, new_post_payload):
    response = posts.create(new_post_payload)

    assert response.status_code == 201
    created = Post.model_validate(response.json())
    assert created.id > 100
    assert created.title == new_post_payload["title"]
    assert created.body == new_post_payload["body"]
    assert created.userId == new_post_payload["userId"]


def test_replace_post(posts):
    payload = {"id": 1, "title": "Replaced title", "body": "Replaced body", "userId": 1}

    response = posts.replace(1, payload)

    assert response.status_code == 200
    replaced = Post.model_validate(response.json())
    assert replaced.title == "Replaced title"
    assert replaced.id == 1


def test_partial_update_keeps_other_fields(posts):
    response = posts.update(1, {"title": "Patched title"})

    assert response.status_code == 200
    patched = Post.model_validate(response.json())
    assert patched.title == "Patched title"
    assert patched.userId == 1
    assert patched.body


def test_delete_post(posts):
    response = posts.delete(1)

    assert response.status_code == 200
    assert response.json() == {}


@pytest.mark.xfail(
    reason="Known limitation: the demo API does not persist writes, so a created post cannot be read back",
    strict=False,
)
def test_created_post_can_be_read_back(posts, new_post_payload):
    created = posts.create(new_post_payload).json()

    response = posts.get(created["id"])

    assert response.status_code == 200
