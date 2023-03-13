from django import forms

from apps.post.models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'cols': 100, 'rows': 20})
        }
