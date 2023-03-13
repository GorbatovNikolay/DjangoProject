from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from apps.user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """UserAdmin with altered user model and added form fields avatar and bio."""
    model = User
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password', 'avatar')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
