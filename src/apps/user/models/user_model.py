from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import RandomCharField
from easy_thumbnails.fields import ThumbnailerImageField


class User(AbstractUser):
    """The model describing the USER. Extends default Django model."""
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_(
            "Обязательное поле."
        ),
    )
    avatar = ThumbnailerImageField(
        _('avatar'),
        upload_to='user/avatars/',
        blank=True,
        help_text=_(
            "Только файлы формата .JPG или .PNG!"
        ),
        resize_source=dict(
            quality=95,
            size=(2000, 2000),
            crop='scale'
        )
    )
    slug = RandomCharField(
        _('user slug'),
        length=12,
        unique=True
    )
    bio = models.TextField(
        _('biography'),
        max_length=1000,
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
