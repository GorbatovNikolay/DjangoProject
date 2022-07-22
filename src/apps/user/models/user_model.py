from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """The model describing the USER. Extends default Django model."""
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_(
            "Обязательное поле."
        ),
    )
    avatar = models.ImageField(
        _('avatar'),
        upload_to='user/avatars/',
        blank=True,
        help_text=_(
            "Только файлы формата .JPG или .PNG! Формат .HEIC на данный момент не поддерживается."
        )
    )
    bio = models.TextField(
        _('biography'),
        blank=True,
        help_text=_(
            "Биография пользователя."
        )
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'User {self.username}'
