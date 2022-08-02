from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from apps.likes.models import Like
from apps.post.models import Post


class LikeView(View):
    """View for liking and unliking posts."""

    def post(self, request, post_slug):
        """Like post if not liked before or unlike if liked."""
        post = get_object_or_404(Post, slug=post_slug)
        user = request.user
        if user.id in post.get_liked_users():
            Like.objects.filter(post=post, user=user).delete()
            return HttpResponseRedirect(self.request.GET.get('next'))
        Like.objects.create(post=post, user=user)
        return HttpResponseRedirect(self.request.GET.get('next'))
