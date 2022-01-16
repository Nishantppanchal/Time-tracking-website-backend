from os import stat
from django.http import request
import rest_framework
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import createUserSerializer, getUserIdSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from users.models import users

# Create your views here.

class customUserCreate(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        print(request.data)
        serializer = createUserSerializer(data=request.data)
        if serializer.is_valid():
            newuser = serializer.save()
            if newuser is not None:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class getUserId(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = getUserIdSerializer
    
    def get_queryset(self):
        user = self.request.user
        userData = users.objects.filter(email=user)
        return userData