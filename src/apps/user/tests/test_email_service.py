from django.test import TestCase

from apps.user.models import User
from apps.user.services import EmailService


class TestEmailService(TestCase):
    def setUp(self) -> None:
        self.user = User(username='test_user', email='test@user.ru', password='12345')
        self.user.save()
        self.current_site = '127.0.0.1:8000'

    def test_write_email_message(self):
        """write_email_message() returns an email message with valid username and activation link."""
        starts_with = '\n    Здравствуйте, test_user,'
        contains = 'http://127.0.0.1:8000/signup/activate/'
        message = EmailService.write_email_message(self.current_site, self.user)
        self.assertIs(message.startswith(starts_with), True)
        self.assertIn(contains, message)
