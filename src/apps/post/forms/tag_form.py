from django import forms

from apps.post.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag_name',)
