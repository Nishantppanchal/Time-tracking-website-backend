from django.db.models import fields
from rest_framework import serializers
from users.models import users

class createUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        print(validated_data)
        user = users.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'], 
            last_name = validated_data['last_name'],
            password = validated_data['password']
        )
        return user
    
class getUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id']  