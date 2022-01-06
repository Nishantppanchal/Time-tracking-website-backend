from django.db import models
from django.db.models.fields.related import ForeignKey
from users.models import users
import datetime
# Create your models here.
    
class labels(models.Model):
    label = models.CharField(max_length=100, default=None, blank=True, null=True)
    user = ForeignKey(users, on_delete=models.CASCADE)
    
class timers(models.Model):
    start_time = models.IntegerField()
    end_time = models.IntegerField(default=None, blank=True, null=True)
    label = models.ManyToManyField(labels)
    user = ForeignKey(users, on_delete=models.CASCADE)