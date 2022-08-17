from django.test import TestCase
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.user.models import User
from apps.user.services import ActivationService
from apps.user.tokens.email_token import account_activation_token


class TestActivationService(TestCase):
    def setUp(self) -> None:
        self.user = User(username='test_user', email='test@user.ru', password='12345')
        self.user.save()
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = account_activation_token.make_token(self.user)

    def test_activate_user(self):
        """activate_user() returns True if id and token are valid."""
        self.assertIs(ActivationService.activate_user(uidb64=self.uidb64, token=self.token), True)

    def test_activate_user_wrong_id(self):
        """activate_user() returns None if id or token are invalid."""
        self.assertIs(ActivationService.activate_user(uidb64=self.uidb64, token='2143'), None)
        self.assertIs(ActivationService.activate_user(uidb64='23415', token=self.token), None)
