from django.contrib.sites.requests import RequestSite
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.user.forms import CustomUserCreationForm
from apps.user.services import EmailService


class SignUpView(CreateView):
    """The view of the registration page."""
    form_class = CustomUserCreationForm
    template_name = 'user/sign_up.html'
    success_url = reverse_lazy('email_info')

    def form_valid(self, form):
        """If the form is valid, save the associated model and send confirmation email."""
        self.object = form.save()
        current_site = RequestSite(self.request).domain
        EmailService.send_confirmation_email(current_site, self.object)
        return super().form_valid(form)
