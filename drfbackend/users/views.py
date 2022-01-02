from os import stat
from django.http import request
import rest_framework
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import createUserSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class customUserCreate(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = createUserSerializer(data=request.data)
        if serializer.is_valid():
            newuser = serializer.save()
            if newuser is not None:
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)