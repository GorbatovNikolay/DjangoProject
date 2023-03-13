from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from apps.post.models import Post


class SinglePostView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Post
    template_name = 'post/single_post.html'
    slug_url_kwarg = 'post_slug'
