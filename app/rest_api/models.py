from django.db import models
from django.db.models.fields import DateField, TextField
from django.db.models.fields.related import ForeignKey
from django.test import TestCase
from users.models import users
import datetime
# Create your models here.
    
class tags(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    billable = models.BooleanField()
    
    user = ForeignKey(users, on_delete=models.CASCADE)
    
class clients(models.Model):
    type = models.CharField(max_length=7, default='clients')
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    
    user = ForeignKey(users, on_delete=models.CASCADE)
class projects(models.Model):
    type = models.CharField(max_length=8, default='projects')
    name = models.CharField(max_length=250)
    colour = models.CharField(max_length=100)
    
    user = ForeignKey(users, on_delete=models.CASCADE)

class logs(models.Model):
    time = models.IntegerField()
    date = models.DateField()
    description = TextField()
    descriptionRaw = TextField()
    
    tags = models.ManyToManyField(tags, blank=True)
    client = models.ForeignKey(clients, blank=True, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(projects, blank=True, null=True, on_delete=models.CASCADE)
    user = ForeignKey(users, on_delete=models.CASCADE)