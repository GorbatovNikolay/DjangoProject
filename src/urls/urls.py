from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .like_urls import urlpatterns as like_urls
from .post_urls import urlpatterns as post_urls
from .user_urls import urlpatterns as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_urls)),
    path('', include(post_urls)),
    path('', include(like_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
