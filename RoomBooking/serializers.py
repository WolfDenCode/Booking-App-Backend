from rest_framework import serializers
from .models import Room, OccupiedDate,RoomImage
from .models import User




class RoomImageSerializer(serializers.ModelSerializer):
    
    room = serializers.HyperlinkedRelatedField(
        view_name='room-detail',
        queryset=Room.objects.all()
    )
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption','room',]
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['url', 'id', 'name', 'type', 'pricePerNight', 'currency', 'maxOccupancy', 'description','images']


class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name='room-detail',
        queryset=Room.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )

    class Meta:
        model = OccupiedDate
        fields = ['url', 'id', 'room', 'user', 'date']


from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username','password','email','full_name']

      # Hash the password before saving     
    def validate_password(self, value):
        return make_password(value)
