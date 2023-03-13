from django.contrib.auth import urls as auth_urls
from django.urls import path

from apps.user.views import (
    ActivateView,
    EmailInfoView,
    SignUpView,
    UserDeleteView,
    UserProfileView,
    UserUpdateView,
)

app_name = 'user'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/email/', EmailInfoView.as_view(), name='email_info'),
    path('signup/activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),

    path(
        'login/',
        auth_urls.views.LoginView.as_view(
            template_name='user/login.html',
            next_page='home',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('logout/', auth_urls.views.LogoutView.as_view(next_page='login'), name='logout'),

    path(
        'password_change/',
        auth_urls.views.PasswordChangeView.as_view(template_name='user/password_change.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_urls.views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),
        name='password_change_done'
    ),

    path(
        'password_reset/',
        auth_urls.views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_urls.views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_urls.views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_urls.views.PasswordResetCompleteView.as_view(template_name='user/password_reset_done.html'),
        name='password_reset_complete'
    ),

    path('user/<slug:user_slug>/', UserProfileView.as_view(), name='profile'),
    path('user/<slug:user_slug>/delete/', UserDeleteView.as_view(), name='delete_user'),
    path('user/<slug:user_slug>/edit/', UserUpdateView.as_view(), name='update_user'),
]
