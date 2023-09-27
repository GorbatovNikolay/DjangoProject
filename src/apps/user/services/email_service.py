from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from celery import shared_task

from apps.user.tokens.email_token import account_activation_token
from settings.settings import EMAIL_HOST_USER


@shared_task
def write_email_message(current_site, user_object) -> str:
    """Writes a message string to use in a confirmation email."""

    message = render_to_string('user/account_activation_email.html', {
        'username': user_object['username'],
        'domain': current_site,
        'user_id': urlsafe_base64_encode(force_bytes(user_object['pk'])),
        'token': account_activation_token.make_token(user_object),
    })
    return message


@shared_task
def send_confirmation_email(current_site, user_object) -> None:
    header = 'Завершение регистрации'
    message = write_email_message(current_site, user_object)
    send_mail(
        header,
        message,
        EMAIL_HOST_USER,
        [user_object['email']],
    )
