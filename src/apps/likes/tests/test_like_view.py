from django.test import TestCase, RequestFactory
from django.urls import reverse

from apps.likes.models import Like
from apps.likes.views import LikeView
from apps.post.models import Post
from apps.user.models import User


class TestLikeView(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='user', email='u@mail.ru', password='112233')
        self.post = Post(body='111', creator=self.user)
        self.post.save()
        self.path = reverse('like_post', kwargs={'post_slug': self.post.slug})
        self.factory = RequestFactory()
        self.request = self.factory.post(self.path)

    def test_like_post_of_other_user(self):
        """LikeView lets user like post of other user."""
        current_user = User.objects.create_user(username='c_user', email='u@email.com', password='1234567')
        self.request.user = current_user
        response = LikeView.as_view()(self.request, post_slug=self.post.slug)
        like = Like.objects.get(post=self.post, user=current_user)
        self.assertIn(like, Like.objects.all())

    def test_like_own_post(self):
        """LikeView lets user like his own post."""
        self.request.user = self.user
        response = LikeView.as_view()(self.request, post_slug=self.post.slug)
        like = Like.objects.get(post=self.post, user=self.user)
        self.assertIn(like, Like.objects.all())

    def test_unlike_post(self):
        """When user already liked a post, LikeView deletes this like object."""
        like = Like(post=self.post, user=self.user)
        like.save()
        self.request.user = self.user
        response = LikeView.as_view()(self.request, post_slug=self.post.slug)
        self.assertNotIn(like, Like.objects.all())
