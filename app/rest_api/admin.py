from django.contrib import admin
from .models import labels, timers
# Register your models here.

admin.site.register(timers)
admin.site.register(labels)