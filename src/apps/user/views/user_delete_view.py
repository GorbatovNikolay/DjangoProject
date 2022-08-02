from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.user.models import User


class UserDeleteView(LoginRequiredMixin, DeleteView):
    """View for user account deletion."""
    model = User
    template_name = 'user/delete_user.html'
    success_url = reverse_lazy('login')
    slug_url_kwarg = 'user_slug'
    login_url = 'login'
