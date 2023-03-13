from django.urls import path

from apps.post.views import (
    HomeView,
    PostCreateView,
    PostDeleteView,
    PostEditView,
    SinglePostView,
)

app_name = 'post'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/<slug:post_slug>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('post/<slug:post_slug>/edit/', PostEditView.as_view(), name='edit_post'),
    path('post/<slug:post_slug>/', SinglePostView.as_view(), name='single_post'),
]
