from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_api.urls')),
    path('api/', include('users.urls')),
    path('openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
