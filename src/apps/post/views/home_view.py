from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ArchiveIndexView

from apps.post.models import Post


class HomeView(LoginRequiredMixin, ArchiveIndexView):
    """View to homepage, shows recent posts."""
    login_url = 'login'
    template_name = 'post/index.html'
    model = Post
    date_field = 'creation_date'
    allow_empty = True
