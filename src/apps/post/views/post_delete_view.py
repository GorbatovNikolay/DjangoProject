from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.post.models import Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')
    slug_url_kwarg = 'post_slug'
    login_url = 'login'
