from rest_framework.permissions import IsAdminUser
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_api.urls')),
    path('api/', include('users.urls')),
    path('docs/', include_docs_urls(title='API documentation'))
]
