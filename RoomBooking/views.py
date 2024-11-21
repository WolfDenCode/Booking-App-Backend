from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Room,OccupiedDate
from .serializers import RoomSerializer,OccupiedDateSerializer,UserSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'rooms': reverse('room-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'occupied-dates': reverse('occupieddate-list', request=request, format=format)
    })



class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]



class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]




class OccupiedDatesList(generics.ListCreateAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OccupiedDatesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSerializer
    permission_classes = [IsAdminOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Save the user
        user = serializer.save()

        # Generate token
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in response
        self.response_data = {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "token": token.key,
        }

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(self.response_data)
    
    # def create(self, request, *args, **kwargs):
    #     super().create(request, *args, **kwargs)
    #     user = User.objects.get(username=request.data['username'])
    #     user.set_password(request.data['password'])
    #     user.save()
    #     token, created = Token.objects.get_or_create(user=user)

    #     # Customize the response to include the token
    #     response_data = {
    #         'user': self.serializer_class(user).data,
    #         'token': token.key,
    #     }
        
    #     return Response(response_data, status=status.HTTP_201_CREATED)
        
        
    
class Login(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TestToken(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer