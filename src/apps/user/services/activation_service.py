from django.contrib.auth import login
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from apps.user.models import User
from apps.user.tokens.email_token import account_activation_token


class ActivationService:
    """Service providing logic to activate a new user."""

    @classmethod
    def activate_user(cls, request, uidb64, token) -> bool:
        """Checks data, gets user by pk, changes is_active to True and returns True if no errors."""
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return True
