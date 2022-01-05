from django.db.models import fields
from rest_framework import serializers
from .models import Test

class serializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['Test']