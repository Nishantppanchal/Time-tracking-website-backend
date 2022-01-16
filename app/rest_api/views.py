from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import clientIdSerializer, clientsCRUDSerializer, logsCRUDSerializer, projectIdSerializer, projectsCRUDSerializer, tagIdSerializer, tagsCRUDSerializer
from .models import clients, logs, projects, tags 
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
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

class clientProjectGet(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request, *args, **kwargs):
        user = request.user
        clientsData = clients.objects.filter(user=user)
        projectsData = projects.objects.filter(user=user)
        
        clientsSerialized = clientsCRUDSerializer(clientsData, many=True)
        projectsSerialized = projectsCRUDSerializer(projectsData, many=True)
        data = clientsSerialized.data + projectsSerialized.data
        
        return Response(data)

class tagsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = tagsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return tags.objects.filter(user=user)
    
    
class getID(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        type = request.query_params.get('type')
        user = request.user
        name = request.query_params.get('name')
        
        if type == 'tag':
            data = tags.objects.get(name=name, user=user)
            id = tagIdSerializer(data)
        if type == 'project':
            data = projects.objects.get(name=name, user=user)
            id = projectIdSerializer(data)
        if type == 'client':
            data = clients.objects.get(name=name, user=user)
            id = clientIdSerializer(data)
        
        return Response(id.data)
        
    
# class timeNow(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = timeNowSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         timeNow = self.request.query_params.get('time_now')
#         return timers.objects.filter(Q(user=user), Q(end_time=None) | Q( end_time__gt=timeNow))
#         # return timers.objects.all()
    
    
    
