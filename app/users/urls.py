from django.urls import path
from .views import customUserCreate, getUserId

app_name = 'user'

urlpatterns = [
    path('user/register/', customUserCreate.as_view(), name='createUser'),
    path('user/id/', getUserId.as_view(), name='getUserId'),
]