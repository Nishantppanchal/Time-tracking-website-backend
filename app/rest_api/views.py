from django.shortcuts import render
from rest_framework import generics
from .serializers import serializer
from .models import Test 
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from django.middleware.csrf import get_token
# Create your views here.

class Test(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Test.objects.all()
    serializer_class = serializer
    
    
