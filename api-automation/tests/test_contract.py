import pytest

pytestmark = pytest.mark.contract

POST_FIELDS = {"userId", "id", "title", "body"}
COMMENT_FIELDS = {"postId", "id", "name", "email", "body"}


def test_post_fields_are_stable(posts):
    body = posts.get(1).json()

    assert set(body) == POST_FIELDS


def test_comment_fields_are_stable(posts):
    comments = posts.comments(1).json()

    for comment in comments:
        assert set(comment) == COMMENT_FIELDS


def test_post_field_types(posts):
    body = posts.get(1).json()

    assert isinstance(body["userId"], int)
    assert isinstance(body["id"], int)
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)
