from django.test import TestCase

from apps.likes.models import Like
from apps.post.models import Post
from apps.user.models import User


class TestPostModel(TestCase):
    def test_get_liked_users(self):
        """get_liked_users() returns all users that likes the post."""
        user = User.objects.create_user(username='user', email='test@mail.ru', password='12345')
        post = Post(creator=user)
        post.save()
        like = Like(post=post, user=user)
        like.save()
        self.assertIn(user.pk, post.get_liked_users())
