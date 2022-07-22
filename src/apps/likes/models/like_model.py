from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.post.models import Post
from apps.user.models import User


class Like(models.Model):
    """Model describing a like object."""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('liked post'),
        help_text=_(
            "Пост, к которому относится лайк."
        )
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('the user that liked the post'),
        help_text=_(
            "Пользователь, поставивший лайк."
        )
    )

    def __str__(self):
        return f'User {self.user.username} liked {self.post}'

    class Meta:
        verbose_name = _('like')
        default_related_name = 'likes'
        order_with_respect_to = 'post'
