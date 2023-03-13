from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ArchiveIndexView

from apps.post.models import Post
from apps.user.models import User


class UserProfileView(LoginRequiredMixin, ArchiveIndexView):
    """View for user profile page."""
    login_url = 'login'
    template_name = 'user/profile.html'
    model = Post
    date_field = 'creation_date'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        context = super().get_context_data()
        context['profile_user'] = User.objects.get(slug=self.kwargs['user_slug'])
        return context

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.model is not None:
            queryset = self.model.objects.filter(creator__slug=self.kwargs['user_slug'])

            if ordering := self.get_ordering():
                if isinstance(ordering, str):
                    ordering = (ordering,)
                queryset = queryset.order_by(*ordering)
            return queryset
