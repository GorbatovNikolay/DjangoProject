from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.user.models import User
from apps.user.tokens.email_token import account_activation_token


class TestActivateView(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', email='testuser@mail.ru', password='12345')
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = account_activation_token.make_token(self.user)

    def test_get_valid_response(self):
        """ActivateView() renders user/account_activation_done.html template if kwargs are valid."""
        path = reverse('activate', kwargs={'uidb64': self.uidb64, 'token': self.token})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/account_activation_done.html')

    def test_get_response_invalid_token(self):
        """ActivateView() returns an HTTPResponse if one of kwargs is invalid."""
        path = reverse('activate', kwargs={'uidb64': self.uidb64, 'token': '12345'})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ссылка активации недействительна!')

    def test_get_response_invalid_id(self):
        """ActivateView() returns an HTTPResponse if one of kwargs is invalid."""
        path = reverse('activate', kwargs={'uidb64': 'a', 'token': self.token})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ссылка активации недействительна!')
