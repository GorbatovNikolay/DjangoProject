from django.views.generic import TemplateView


class EmailInfoView(TemplateView):
    """The view to the page informing that the confirmation link was sent."""
    template_name = 'user/email_confirmation_info.html'
