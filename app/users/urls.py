from django.urls import path
from .views import customUserCreate

app_name = 'user'

urlpatterns = [
    path('user/register/', customUserCreate.as_view(), name='createUser')
]