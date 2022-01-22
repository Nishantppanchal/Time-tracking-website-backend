from django.db.models import fields
from rest_framework import serializers
from .models import logs, clients, projects, tags

class logsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = logs
        fields = ['id', 'time', 'date', 'description', 'tags', 'client', 'project', 'user']
        
class clientsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ['id', 'type', 'name', 'colour', 'user']    
        
class projectsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ['id', 'type', 'name', 'colour', 'user']        
    
    
class tagsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = tags
        fields = ['id', 'name', 'billable', 'user']   
        
    
class tagIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = tags
        fields = ['id']
        

class clientIdSerializer(serializers.ModelSerializer):
    class Meta:
        models = clients
        fields = ['id']

class projectIdSerializer(serializers.ModelSerializer):
    class Meta:
        models = projects
        fields = ['id']
    
# class timeNowSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = timers
#         fields = ['start_time', 'label', 'user', 'end_time', 'id']