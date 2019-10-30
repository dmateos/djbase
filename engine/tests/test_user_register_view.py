import pytest
from django.test import Client
from django.urls import reverse

from engine.models import Account


def test_client():
    return Client()


@pytest.mark.django_db
def test_user_register_page_loads():
    response = test_client().get(reverse("user_register"))

    assert response.status_code == 200
    assert "Username" in str(response.content)
    assert "Password" in str(response.content)
    assert "Email address" in str(response.content)


@pytest.mark.django_db
def test_user_can_register():
    response = test_client().post(
        reverse("user_register"),
        {"username": "test", "password": "test", "email": "test@test.com"},
        follow=True,
    )

    assert "Login successful" in str(response.content)
    assert "Logout" in str(response.content)
    assert Account.objects.filter(name="test").first() is not None


@pytest.mark.django_db
def test_associated_account_is_created():
    test_client().post(
        reverse("user_register"),
        {"username": "test", "password": "test", "email": "test@test.com"},
        follow=True,
    )

    assert Account.objects.filter(name="test").first().user.username == "test"
