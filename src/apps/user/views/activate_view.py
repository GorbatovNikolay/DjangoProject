from django.http import HttpResponse
from django.views import View

from apps.user.services import ActivationService


class ActivateView(View):
    """The view of the page to which the email confirmation link leads."""

    def get(self, request, uidb64, token):
        if ActivationService.activate_user(request, uidb64, token):
            return HttpResponse('Регистрация прошла успешно. Теперь вы можете войти.')
        return HttpResponse('Ссылка активации недействительна!')
