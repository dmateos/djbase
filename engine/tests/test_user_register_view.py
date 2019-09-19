from django.test import TestCase

# from django.test.utils import setup_test_environment
from django.urls import reverse
from engine.models import Account


class UserRegisterViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_register_page_loads(self):
        response = self.client.get(reverse("user_register"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")
        self.assertContains(response, "Email address")

    def test_user_can_register(self):
        response = self.client.post(
            reverse("user_register"),
            {"username": "test", "password": "test", "email": "test@test.com"},
            follow=True,
        )

        self.assertContains(response, "Login successful")
        self.assertContains(response, "Logout")
        assert Account.objects.filter(name="test").first() != None

    def test_associated_account_is_created(self):
        response = self.client.post(
            reverse("user_register"),
            {"username": "test", "password": "test", "email": "test@test.com"},
            follow=True,
        )
        assert Account.objects.filter(name="test").first().user.username == "test"
