# Imports the required components
from django.urls.conf import include
from django.urls import path
from .views import changePassword, customUserCreate, getUser, userPartialUpdate

# Sets the app name
app_name = 'user'


# Creates API endpoints
urlpatterns = [
    # URL to create user
    path('user/register/', customUserCreate.as_view(), name='createUser'),
    # URL to get user ID
    path('user/id/', getUser.as_view(), name='getUser'),
    # URL to change password
    path('user/change-password/', changePassword.as_view(), name='changePassword'),
    # URL for user update
    path('user/update/', userPartialUpdate.as_view(), name='updateUserDetails')
]