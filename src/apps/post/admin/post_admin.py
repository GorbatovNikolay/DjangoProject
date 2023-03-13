from django.contrib import admin

from apps.post.models import Post
from .photo_admin import PhotoAdmin
from .tag_admin import TagAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin, TagAdmin]
