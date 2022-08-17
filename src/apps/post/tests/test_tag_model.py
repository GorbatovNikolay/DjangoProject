from django.test import TestCase

from apps.post.models import (
    Post,
    Tag
)
from apps.user.models import User


class TestTagModel(TestCase):
    def test_get_number_of_tags(self):
        """_get_number_of_tags() returns number of tags of the post."""
        user = User.objects.create_user(username='user', email='test@mail.ru', password='12345')
        post = Post(creator=user)
        post.save()
        tag = Tag(tag_name='tag', post=post)
        tag.save()
        self.assertEqual(Tag._get_number_of_tags(tag), 1)
