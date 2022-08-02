from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.user.forms import UserUpdateForm
from apps.user.models import User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """View for user profile editing page."""
    model = User
    form_class = UserUpdateForm
    template_name = 'user/update_user.html'
    login_url = 'login'
    slug_url_kwarg = 'user_slug'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_slug': self.object.slug})
