from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from apps.post.processors import FilePathProcessor
from .post_model import Post


class Photo(models.Model):
    """Model describing a photo of the post."""
    image = ThumbnailerImageField(
        _('post image'),
        upload_to=FilePathProcessor.get_photo_path,
        resize_source=dict(
            quality=95,
            size=(1290, 2048),
            crop='scale'
        )
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('photo post'),
        related_name='photos',
        help_text=_(
            "Пост, к которому относится изображение."
        )
    )

    def __str__(self):
        return f'Photo id={self.id}.'

    def clean(self):
        if self._get_number_of_photos(self) > 10:
            raise ValidationError("Post already has 10 photos!")

    class Meta:
        verbose_name = _('photo')
        order_with_respect_to = 'post'

    @staticmethod
    def _get_number_of_photos(photo):
        return photo.post.photos.count()
