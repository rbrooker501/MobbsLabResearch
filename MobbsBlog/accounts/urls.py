from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, ChangedPasswordView, ShowProfileView, EditProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', ChangePasswordView.as_view(template_name='registration/change-password.html')),
    path('password_changed/', ChangedPasswordView, name='password-changed'),
    path('<int:pk>/profile', ShowProfileView.as_view(), name='show-profile'),
    path('<int:pk>/profile/edit', EditProfileView.as_view(), name='edit-profile-page'),
]