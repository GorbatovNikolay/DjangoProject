from django.contrib import admin

from apps.post.models import Tag


class TagAdmin(admin.TabularInline):
    model = Tag
    extra = 1
    max_num = 5
