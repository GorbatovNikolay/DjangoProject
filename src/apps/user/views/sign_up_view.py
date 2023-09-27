from django.contrib.sites.requests import RequestSite
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.user.forms import CustomUserCreationForm
from apps.user.services.email_service import send_confirmation_email


class SignUpView(CreateView):
    """The view of the registration page."""
    form_class = CustomUserCreationForm
    template_name = 'user/sign_up.html'
    success_url = reverse_lazy('email_info')

    def form_valid(self, form):
        """If the form is valid, save the associated model and send confirmation email."""
        self.object = form.save()
        current_site = RequestSite(self.request).domain

        user_data = {
            'username': self.object.username,
            'pk': self.object.pk,
            'email': self.object.email,
            'is_active': self.object.is_active
        }

        send_confirmation_email.delay(current_site, user_data)
        return super().form_valid(form)
