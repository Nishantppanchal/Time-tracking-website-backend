from django.db.models import fields
from rest_framework import serializers
from .models import timers

class timerCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = timers
        fields = ['start_time', 'label', 'user', 'end_time']
        
class timeNowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = timers
        fields = ['start_time', 'label', 'user', 'end_time']