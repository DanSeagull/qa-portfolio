import pytest

pytestmark = [pytest.mark.regression, pytest.mark.negative]


@pytest.mark.parametrize("post_id", [9999, 0, -1, "abc"])
def test_get_missing_post_returns_404(posts, post_id):
    response = posts.get(post_id)

    assert response.status_code == 404


def test_unknown_endpoint_returns_404(api_client):
    response = api_client.get("/does-not-exist")

    assert response.status_code == 404


def test_filter_by_unknown_user_returns_empty_list(posts):
    response = posts.list(userId=999)

    assert response.status_code == 200
    assert response.json() == []
