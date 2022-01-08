from django.db.models import fields
from rest_framework import serializers
from .models import logs, clients, projects

class logsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = logs
        fields = ['time', 'description', 'tags', 'client', 'project', 'user']
        
class clientsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ['type', 'name', 'colour', 'user']    
        
class projectsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ['type', 'name', 'colour', 'user']        
    
    
    
# class timeNowSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = timers
#         fields = ['start_time', 'label', 'user', 'end_time', 'id']