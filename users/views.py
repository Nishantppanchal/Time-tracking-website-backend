# Import required components
from cmath import acos
from email import message
import email
from django.http import request
import rest_framework
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import createUserSerializer, getUserSerializer, userPartialUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from users.models import users
from rest_framework import viewsets

# View for creating user
class customUserCreate(APIView):
    # Allows anyone to use this endpoint
    permission_classes = [AllowAny]
    
    # Defines how to handles a post request
    def post(self, request):
        # Data is run through the serialiser
        serializer = createUserSerializer(data=request.data)
        # If the data is serialisable
        if serializer.is_valid():
            # Save the data to the log model
            newUser = serializer.save()
            # If there is not a error creating the user
            if newUser is not None:
                # Return a 201 created status code
                return Response(status=status.HTTP_201_CREATED)
        # If the data is not serialisable
        # Return the errors and a 400 bad request status code
        return Response(status=status.HTTP_400_BAD_REQUEST)

# View for getting user id   
class getUser(generics.ListAPIView):
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    # Sets the serializer
    serializer_class = getUserSerializer
    
    # Customizes what data is retrieved
    def get_queryset(self):
        # Sets the user ID from the request
        user = self.request.user
        
        # Filters the user table for the user's data
        userData = users.objects.filter(email=user)
        
        # Returns the user's data
        return userData
    
class userPartialUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userPartialUpdateSerializer
    
    def get_object(self):
        email = self.request.user
        return users.objects.get(email=email)
        
    def update(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        print(request.headers)
        if str(user) == data.get('email', None):
            del data['email']
        # elif users.objects.filter(email=data.get('email', '')).len() > 0:
            
        
        
        serializer = self.serializer_class(user, data=data, partial=True)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_200_OK)
            
class changePassword(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
    
        try:
            newPassword = request.data['new_password']
        except:
            return Response({ message: 'new_password field required' }, status=status.HTTP_400_BAD_REQUEST)
    
        if user.check_password(newPassword):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(newPassword)
        user.save()
        return Response(status=status.HTTP_202_ACCEPTED)