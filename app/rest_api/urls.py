from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import clientProjectGet, clientsCRUD, logsCRUD, projectsCRUD, tagsCRUD, doesTagExist

router = DefaultRouter()
router.register('logs', logsCRUD, basename='logsCRUD')
router.register('clients', clientsCRUD, basename='clientsCRUD')
router.register('projects', projectsCRUD, basename='projectsCRUD')
router.register('tags', tagsCRUD, basename='tagsCRUD')

urlpatterns = [
    path('auth/', include('rest_framework_social_oauth2.urls')),
    # path('timerNow/', timeNow.as_view()),
    path('CRUD/', include(router.urls)),
    path('clientProjectGet/', clientProjectGet.as_view()),
    path('doesTagExist/', doesTagExist.as_view())
]