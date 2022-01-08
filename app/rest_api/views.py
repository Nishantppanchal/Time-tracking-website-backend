from django.shortcuts import render
from rest_framework import generics
from .serializers import clientsCRUDSerializer, logsCRUDSerializer, projectsCRUDSerializer
from .models import clients, logs, projects 
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import viewsets
from django.db.models import Q
# Create your views here.

class logsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = logsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return logs.objects.filter(user=user)
    
class clientsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = clientsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return clients.objects.filter(user=user)
    
class projectsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = projectsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return projects.objects.filter(user=user)

    
# class timeNow(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = timeNowSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         timeNow = self.request.query_params.get('time_now')
#         return timers.objects.filter(Q(user=user), Q(end_time=None) | Q( end_time__gt=timeNow))
#         # return timers.objects.all()
    
    
    
