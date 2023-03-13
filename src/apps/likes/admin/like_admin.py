from django.contrib import admin

from apps.likes.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
