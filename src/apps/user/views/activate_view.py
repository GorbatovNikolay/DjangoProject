from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.user.services import ActivationService


class ActivateView(View):
    """The view of the page to which the email confirmation link leads."""

    def get(self, request, uidb64, token):
        if ActivationService.activate_user(uidb64, token):
            return render(request, 'user/account_activation_done.html')
        return HttpResponse('Ссылка активации недействительна!')
