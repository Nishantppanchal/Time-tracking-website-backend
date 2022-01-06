from django.shortcuts import render
from rest_framework import generics
from .serializers import timerCRUDSerializer, timeNowSerializer
from .models import timers 
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import viewsets
from django.db.models import Q
# Create your views here.

class timerCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = timerCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return timers.objects.filter(user=user)
    
class timeNow(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = timeNowSerializer
    
    def get_queryset(self):
        user = self.request.user
        timeNow = self.request.query_params.get('time_now')
        return timers.objects.filter(Q(user=user), Q(end_time=None) | Q( end_time__gt=timeNow))
    
    
    
    
