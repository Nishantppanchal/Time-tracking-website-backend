from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import timerCRUD, timeNow

router = DefaultRouter()
router.register('', timerCRUD, basename='timerCRUD')

urlpatterns = [
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('timerNow/', timeNow.as_view()),
    path('timerCRUD/', include(router.urls)),
]