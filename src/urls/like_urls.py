from django.urls import path

from apps.likes.views import LikeView

app_name = 'likes'
urlpatterns = [
    path('like/<slug:post_slug>/', LikeView.as_view(), name='like_post'),
]
