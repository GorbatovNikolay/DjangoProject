from django.urls import reverse_lazy

from .base_post_create_edit_view import BasePostCreateEditView


class PostEditView(BasePostCreateEditView):
    """View for post editing page."""
    login_url = 'login'
    success_url = reverse_lazy('home')
    template_name = 'post/edit_post.html'
