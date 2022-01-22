from genericpath import exists
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import clientIdSerializer, clientsCRUDSerializer, logsCRUDSerializer, projectIdSerializer, projectsCRUDSerializer, tagIdSerializer, tagsCRUDSerializer
from .models import clients, logs, projects, tags 
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework import viewsets
from django.db.models import Q
from rest_framework import status
# Create your views here.

class logsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = logsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        number = int(self.request.query_params.get('number'))
        start = number
        end = number + 100
        count = logs.objects.filter(user=user).count() - 1
        if end <= count:
            return logs.objects.filter(user=user).order_by('-date')[start:end]
        elif start <= count:
            return logs.objects.filter(user=user).order_by('-date')[start:]
        else:
            return logs.objects.filter(user=user).none()
    
    def create(self, request):
        serializer = logsCRUDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            log = serializer.data
            return Response(log, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class clientsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = clientsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return clients.objects.filter(user=user)
    
    def create(self, request):
        serializer = clientsCRUDSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            return Response(client, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class projectsCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = projectsCRUDSerializer
    
    def get_queryset(self):
        user = self.request.user
        return projects.objects.filter(user=user)
    
    def create(self, request):
        serializer = projectsCRUDSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(project, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
    
    def create(self, request):
        serializer = tagsCRUDSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            tag = serializer.data
            return Response(tag, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class doesTagExist(generics.GenericAPIView): 
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        name = request.query_params.get('name')
        print(tags.objects.filter(user=user, name=name).exists())
        if tags.objects.filter(user=user, name=name).exists(): 
            data = {'exists': True, 'id': tags.objects.filter(user=user, name=name)[0].id}# the [0] is to prevent accidential duplicates causing errors
        else:
            data = {'exists': False}
            
        return Response(data)
            
        

# class timeNow(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = timeNowSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         timeNow = self.request.query_params.get('time_now')
#         return timers.objects.filter(Q(user=user), Q(end_time=None) | Q( end_time__gt=timeNow))
#         # return timers.objects.all()
    
    
    
