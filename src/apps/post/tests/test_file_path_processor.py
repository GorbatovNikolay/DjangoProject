from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase

from apps.post.models import (
    Post,
    Photo
)
from apps.post.processors import FilePathProcessor
from apps.user.models import User


class TestFilePathProcessor(TestCase):
    def test_get_photo_path(self):
        """Returns a path for storing uploaded photos."""
        user = User.objects.create_user(username='user', email='test@mail.ru', password='12345')
        post = Post(creator=user)
        post.save()
        im = Image.new(mode='RGB', size=(200, 200))
        im_io = BytesIO()
        im.save(im_io, 'JPEG')
        im_io.seek(0)
        image = InMemoryUploadedFile(
            im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None
        )
        photo = Photo(image=image, post=post)
        photo.save()
        self.assertEqual(
            FilePathProcessor.get_photo_path(photo, 'random-name.jpg'),
            f'post/photos/post_{post.id}/random-name.jpg'
        )
