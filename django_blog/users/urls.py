from django.urls import path
from django.contrib.auth import views as auth_views
from . forms import UserLoginForm
from . import views

urlpatterns = [
    # url for account creation
    path('register/', views.RegisterView.as_view(), name='users-register'),
    # url for login
    path('login/', auth_views.LoginView.as_view(
        # authentication_form=UserLoginForm,
        template_name='users/login.html'), name='users-login'),
    # url for loggin out
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    # url for viewing profiles
    path('profile/<username>', views.ProfileView.as_view(), name='users-profile'),
    # url for updating profiles
    path('profile/update/', views.ProfileUpdateView.as_view(), name='users-profile-update'),
    # url for password reset view
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    # password reset done
    path('password-reset/email-sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    # password changing
    path('password-reset/change-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_change.html'), name='password_reset_confirm'),
    # password changing
    path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_confirm_done.html'), name='password_reset_confirm_done')
]
