import pytest

from api_tests.models import User

pytestmark = pytest.mark.regression


@pytest.mark.smoke
def test_list_users(users):
    response = users.list()

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 10
    for item in items:
        User.model_validate(item)


def test_get_user(users):
    response = users.get(1)

    assert response.status_code == 200
    user = User.model_validate(response.json())
    assert user.id == 1
    assert "@" in user.email
