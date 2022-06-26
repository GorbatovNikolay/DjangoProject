from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .user_urls import urlpatterns as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
