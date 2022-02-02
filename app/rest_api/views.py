# Imports the required components
from rest_framework import generics
from rest_framework.response import Response
from .serializers import clientsCRUDSerializer, logsCRUDSerializer, projectsCRUDSerializer, tagsCRUDSerializer
from .models import clients, logs, projects, tags 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status

# View for logs CRUD
class logsCRUD(viewsets.ModelViewSet):
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    # Sets the serializer
    serializer_class = logsCRUDSerializer
    
    # Customizes what data is retrieved
    def get_queryset(self):
        # Sets the attribute number from the params in the URL
        number = self.request.query_params.get('number')
        # Sets the user ID from the request
        user = self.request.user
        
        # If the number is None
        if number is None: 
            # Return all the logs in one go
            return logs.objects.filter(user=user)
        # Otherwise progressively return the logs
        else:
            # Sets the start log to the integer number
            start = int(number)
            # Sets the end log to the integer number + 100 
            end = int(number) + 100
            # Gets the index of the last log (start from zero)
            count = logs.objects.filter(user=user).count() - 1
            
            # If the end log is within all the logs 
            if end <= count:
                # Return all the logs from the start log to the log before the end log
                return logs.objects.filter(user=user).order_by('-date')[start:end]
            # If the start log is within all the logs
            elif start <= count:
                # Return all the logs after and including the start log 
                return logs.objects.filter(user=user).order_by('-date')[start:]
            # Otherwise, if both the start log and end log are not within all the logs
            else:
                # Return a empty list
                return logs.objects.filter(user=user).none()
    
    # Customizes what happens on a post request
    def create(self, request):
        # Data is run through the serialiser
        serializer = logsCRUDSerializer(data=request.data)
        # If the data is serialisable
        if serializer.is_valid():
            # Save the data to the log model
            serializer.save()
            # Gets the log created
            log = serializer.data
            # Return the log created and a 201 created status code
            return Response(log, status=status.HTTP_201_CREATED)
        # If the data is not serialisable
        # Return the errors and a 400 bad request status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# View for clients CRUD
class clientsCRUD(viewsets.ModelViewSet):
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    # Sets the serializer
    serializer_class = clientsCRUDSerializer
    
    # Customizes what data is retrieved
    def get_queryset(self):
        # Sets the user ID from the request
        user = self.request.user
        # Returns the user's clients
        return clients.objects.filter(user=user)
    
    # Customizes what happens on a post request
    def create(self, request):
        # Data is run through the serialiser
        serializer = clientsCRUDSerializer(data=request.data)
        # If the data is serialisable
        if serializer.is_valid():
            # Save the data to the clients model
            client = serializer.save()
            # Return the client created and a 201 created status code
            return Response(client, status=status.HTTP_201_CREATED)
        # If the data is not serialisable
        # Return the errors and a 400 bad request status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# View for projects CRUD
class projectsCRUD(viewsets.ModelViewSet):
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    # Sets the serializer
    serializer_class = projectsCRUDSerializer
    
    # Customizes what data is retrieved
    def get_queryset(self):
        # Sets the user ID from the request
        user = self.request.user
        # Returns the user's projects
        return projects.objects.filter(user=user)
    
    # Customizes what happens on a post request
    def create(self, request):
        # Data is run through the serialiser
        serializer = projectsCRUDSerializer(data=request.data)
        # If the data is serialisable
        if serializer.is_valid():
            # Save the data to the projects model
            project = serializer.save()
            # Return the client created and a 201 created status code
            return Response(project, status=status.HTTP_201_CREATED)
        # If the data is not serialisable
        # Return the errors and a 400 bad request status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
# View for tags CRUD
class tagsCRUD(viewsets.ModelViewSet):
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    # Sets the serializer
    serializer_class = tagsCRUDSerializer
    
    # Customizes what data is retrieved
    def get_queryset(self):
        # Sets the user ID from the request
        user = self.request.user
        # Returns the user's tags
        return tags.objects.filter(user=user)
    
    # Customizes what happens on a post request
    def create(self, request):
        # Data is run through the serialiser
        serializer = tagsCRUDSerializer(data=request.data)
        # If the data is serialisable
        if serializer.is_valid():
            # Save the data to the projects model
            serializer.save()
            # Gets the tag created
            tag = serializer.data
            # Return the tag created and a 201 created status code
            return Response(tag, status=status.HTTP_201_CREATED)
        # If the data is not serialisable
        # Return the errors and a 400 bad request status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# Creates a generic endpoint to get all the user's clients and projects
class clientProjectGet(generics.GenericAPIView):
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    
    # Defines what happens on a get request
    def get(self, request, *args, **kwargs):
        # Sets the user ID from the request
        user = request.user
        # Filters the clients table for the user's clients
        clientsData = clients.objects.filter(user=user)
        # Filters the projects table for the user's projects 
        projectsData = projects.objects.filter(user=user)
        
        # Serialises the user's clients
        clientsSerialized = clientsCRUDSerializer(clientsData, many=True)
        # Serializers the user's projects
        projectsSerialized = projectsCRUDSerializer(projectsData, many=True)
        # Combines the serializered data
        data = clientsSerialized.data + projectsSerialized.data
        
        # Return the data to the frontend
        return Response(data)

# Creates a generic endpoint to check whether a tag exists
class doesTagExist(generics.GenericAPIView): 
    # Requires authentication to access this endpoint
    permission_classes = [IsAuthenticated]
    
    # Defines what happens on a get request
    def get(self, request, *args, **kwargs):
        # Sets the user ID from the request
        user = request.user
        # Sets the attribute name from the params in the URL
        name = request.query_params.get('name')
        
        # If a tag with the name specificed made by the user specificed exists
        if tags.objects.filter(user=user, name=name).exists(): 
            # Sets data to a dictionary with exists as true and the id as the tag id
            data = {'exists': True, 'id': tags.objects.filter(user=user, name=name)[0].id}# the [0] is to prevent accidential duplicates causing errors
        else:
            # Sets data to a dictionary with exists as false
            data = {'exists': False}
            
        # Return the data to the frontend
        return Response(data)
            
    
    
    
