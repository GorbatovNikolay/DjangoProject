import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailTokenGenerator(PasswordResetTokenGenerator):
    """Creation of the token for the user registration."""

    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user['pk']) + six.text_type(timestamp) +
                six.text_type(user['is_active'])
        )


account_activation_token = EmailTokenGenerator()
