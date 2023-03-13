from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase

from apps.post.models import Post, Photo
from apps.user.models import User


class TestPhotoModel(TestCase):
    def test_get_number_of_photos(self):
        """_get_number_of_photos() returns number of photos of the post."""
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
        self.assertEqual(Photo._get_number_of_photos(photo), 1)
