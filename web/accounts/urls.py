from django.urls import path

from web.accounts.views import UserRegistrationView, UserLoginView, logout_view, ProfileDetailsView, \
    CreateUserProfileView, EditProfileView, DeleteProfileView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('profile-create/', CreateUserProfileView.as_view(), name='profile create'),
    path('profile-edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),
    path('profile-delete/<int:pk>/', DeleteProfileView.as_view(), name='profile delete')

)