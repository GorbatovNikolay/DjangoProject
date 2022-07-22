from django.urls import reverse_lazy

from .base_post_create_edit_view import BasePostCreateEditView


class PostCreateView(BasePostCreateEditView):
    """View for post creating page."""
    login_url = 'login'
    success_url = reverse_lazy('home')
    template_name = 'post/create_post.html'
