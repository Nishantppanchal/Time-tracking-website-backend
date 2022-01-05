from django.urls import path
from django.urls.conf import include
from .views import Test

urlpatterns = [
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('test/', Test.as_view())
]