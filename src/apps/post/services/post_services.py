from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404

from apps.post.forms import (
    TagForm,
    PhotoForm, PostCreationForm,
)
from apps.post.models import (
    Post,
    Tag,
    Photo,
)


class PostService:
    """Service for creating and editing posts."""

    @classmethod
    def save_objects(cls, post_form, photo_formset, tag_formset, request=None) -> None:
        """Either gets forms to existing objects and saves them to edit post
        or creates objects post, photos and tags from valid forms and request."""
        if post_form.instance.pk is not None:
            post_form.save()
            tag_formset.save()
            photo_formset.save()
        else:
            post = post_form.save(commit=False)
            post.creator = request.user
            post.save()
            tag_formset.instance = post
            tag_formset.save()
            photo_formset.instance = post
            photo_formset.save()

    @classmethod
    def get_forms(cls, request, slug=None) -> tuple:
        """Returns forms depending on the request method for editing if post slug is provided
        or for creating a new post if it is not."""
        PhotoFormSet, TagFormSet, post_instance = None, None, None

        if slug:
            post_instance = get_object_or_404(Post, slug=slug)
            PhotoFormSet, TagFormSet = cls.get_formset(delete=True)
        else:
            PhotoFormSet, TagFormSet = cls.get_formset()

        if request.method == 'POST':
            post_form = PostCreationForm(request.POST, instance=post_instance)
            photo_formset = PhotoFormSet(request.POST, request.FILES, instance=post_instance)
            tag_formset = TagFormSet(request.POST, instance=post_instance)
            return post_form, photo_formset, tag_formset

        post_form = PostCreationForm(instance=post_instance)
        photo_formset = PhotoFormSet(instance=post_instance)
        tag_formset = TagFormSet(instance=post_instance)
        return post_form, photo_formset, tag_formset

    @staticmethod
    def get_formset(delete: bool = False) -> tuple:
        """Returns formset factories."""
        TagFormSet = inlineformset_factory(
            Post,
            Tag,
            form=TagForm,
            extra=5,
            max_num=5,
            can_delete=delete
        )
        PhotoFormSet = inlineformset_factory(
            Post,
            Photo,
            form=PhotoForm,
            min_num=1,
            max_num=10,
            extra=10,
            can_delete=delete
        )
        return PhotoFormSet, TagFormSet
