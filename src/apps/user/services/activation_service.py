from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from apps.user.models import User
from apps.user.tokens.email_token import account_activation_token


class ActivationService:
    """Service providing logic to activate a new user."""

    @classmethod
    def activate_user(cls, uidb64, token) -> bool | None:
        """Checks data, gets user by pk, changes is_active to True and returns True if no errors."""
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        user_data = {
            'username': user.username,
            'pk': user.pk,
            'email': user.email,
            'is_active': user.is_active
        }

        if user is not None and account_activation_token.check_token(user_data, token):
            user.is_active = True
            user.save()
            return True
