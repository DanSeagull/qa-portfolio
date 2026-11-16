import pytest

from api_tests.models import Comment, Post

pytestmark = pytest.mark.regression


@pytest.mark.smoke
def test_list_posts_returns_100_valid_posts(posts):
    response = posts.list()

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 100
    for item in items:
        Post.model_validate(item)


@pytest.mark.smoke
def test_get_single_post(posts):
    response = posts.get(1)

    assert response.status_code == 200
    post = Post.model_validate(response.json())
    assert post.id == 1
    assert post.userId == 1


def test_response_content_type_is_json(posts):
    response = posts.get(1)

    assert "application/json" in response.headers["content-type"]


@pytest.mark.parametrize("user_id", range(1, 11))
def test_filter_posts_by_user(posts, user_id):
    response = posts.list(userId=user_id)

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 10
    assert {item["userId"] for item in items} == {user_id}


def test_post_comments_belong_to_the_post(posts):
    response = posts.comments(1)

    assert response.status_code == 200
    comments = [Comment.model_validate(item) for item in response.json()]
    assert len(comments) == 5
    assert all(comment.postId == 1 for comment in comments)
    assert all("@" in comment.email for comment in comments)
