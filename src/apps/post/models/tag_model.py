from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .post_model import Post


class Tag(models.Model):
    """Model describing a tag of the post."""
    tag_name = models.CharField(
        _('tag name'),
        max_length=20,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('tag post'),
        related_name='tags',
        help_text=_(
            "Пост, к которому относится тег."
        )
    )

    def __str__(self):
        return f'Tag name - {self.tag_name}.'

    def clean(self):
        if self._get_number_of_tags(self) > 5:
            raise ValidationError("Post already has 5 tags!")

    class Meta:
        verbose_name = _('tag')
        order_with_respect_to = 'post'

    @staticmethod
    def _get_number_of_tags(tag):
        return tag.post.tags.count()
