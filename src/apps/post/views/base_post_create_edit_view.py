from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from apps.post.services import PostService


class BasePostCreateEditView(LoginRequiredMixin, View):
    """Base view for creating or editing post."""
    template_name = None
    success_url = None

    def get_context_data(self, request, post_slug) -> dict:
        """Gets forms and puts them into context dictionary."""
        post_form, photo_formset, tag_formset = PostService.get_forms(request, slug=post_slug)
        return {
            'post_form': post_form,
            'tag_formset': tag_formset,
            'photo_formset': photo_formset
        }

    def get(self, request, post_slug=None):
        """Renders a template with either empty or filled forms for 'GET' query."""
        context = self.get_context_data(request, post_slug)
        return render(request, self.template_name, context)

    def post(self, request, post_slug=None):
        """Renders a template with either empty or filled forms for 'POST' query,
        if forms are valid, saves them."""
        if self.template_name is None:
            raise AttributeError('Template name is not defined!')
        if self.success_url is None:
            raise AttributeError('Success url is not defined!')

        context = self.get_context_data(request, post_slug)
        post_form, photo_formset, tag_formset = context.values()

        if post_form.is_valid() and photo_formset.is_valid() and tag_formset.is_valid():
            PostService.save_objects(
                post_form,
                photo_formset,
                tag_formset,
                request
            )
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, context)
