from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db import models as extension_models
from django_extensions.db.fields import RandomCharField

from apps.user.models import User


class Post(models.Model):
    """Model describing a post."""
    body = models.TextField(
        _('post body'),
        max_length=2000,
        blank=True,
        help_text=_(
            "Добавьте текст поста."
        )
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('creator of the post'),
        related_name='posts',
        help_text=_(
            "Создатель поста."
        )
    )
    post_likes = models.ManyToManyField(
        User,
        through='likes.Like',
        verbose_name=_('likes'),
        help_text=_(
            "Лайки, поставленные посту."
        )
    )
    slug = RandomCharField(
        _('post slug'),
        length=12,
        unique=True
    )
    creation_date = extension_models.CreationDateTimeField()

    def __str__(self):
        return f'{self.creator.username}\'s post №' \
               f'{list(self.creator.posts.values_list("id", flat=True)).index(self.id) + 1}.'

    def get_liked_users(self) -> list:
        """Returns a list of users that liked the post."""
        return [like.user for like in self.likes.all()]

    class Meta:
        verbose_name = _('post')
        order_with_respect_to = 'creator'
