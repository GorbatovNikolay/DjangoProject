from django import forms

from apps.user.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'bio',
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 50, 'rows': 20})
        }
