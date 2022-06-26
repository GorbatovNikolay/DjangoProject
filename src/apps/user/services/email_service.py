from django.contrib.sites.requests import RequestSite
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.user.tokens.email_token import account_activation_token
from settings.settings import EMAIL_HOST_USER


class EmailService:
    """Service providing functionality to send a confirmation email."""

    @classmethod
    def write_email_message(cls, request, user_object) -> str:
        """Writes a message string to use in a confirmation email."""
        current_site = RequestSite(request).domain
        message = render_to_string('user/account_activation_email.html', {
            'username': user_object.username,
            'domain': current_site,
            'user_id': urlsafe_base64_encode(force_bytes(user_object.pk)),
            'token': account_activation_token.make_token(user_object),
        })
        return message

    @classmethod
    def send_confirmation_email(cls, request, user_object) -> None:
        message = cls.write_email_message(request, user_object)
        send_mail(
            'Завершение регистрации',
            message,
            EMAIL_HOST_USER,
            [user_object.email],
            fail_silently=False,
        )
