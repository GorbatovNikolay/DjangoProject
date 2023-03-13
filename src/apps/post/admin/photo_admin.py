from django.contrib import admin

from apps.post.models import Photo


class PhotoAdmin(admin.TabularInline):
    model = Photo
    extra = 1
