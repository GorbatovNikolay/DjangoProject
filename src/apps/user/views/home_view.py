from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View


class HomeView(LoginRequiredMixin, View):
    """Temporary view to homepage."""
    login_url = 'login'

    def get(self, request):
        return HttpResponse('HOME')
