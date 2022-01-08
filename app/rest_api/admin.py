from django.contrib import admin
from .models import clients, projects, tags, logs
# Register your models here.

admin.site.register(logs)
admin.site.register(tags)
admin.site.register(clients)
admin.site.register(projects)