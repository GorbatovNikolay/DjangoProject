from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.user.models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form. Added email field."""
    email = forms.EmailField(
        max_length=254,
        help_text='Обязательное поле. Пожалуйста, введите адрес электронной почты.'
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
