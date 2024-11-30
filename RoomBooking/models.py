from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

from cloudinary.models import CloudinaryField
    
class Room(models.Model):
    ROOM_TYPES = [
        ('suite', 'Suite'),
        ('standard', 'Standard Room'),
        ('deluxe', 'Deluxe Room'),
    ]
    CURRENCY_TYPES = [
        ('USD', 'USD'),
        ('USD', 'EUR'),
    ]
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, choices=ROOM_TYPES)
    pricePerNight = models.IntegerField(default=150)
    currency = models.CharField(default="USD", max_length=10, choices=CURRENCY_TYPES)
    maxOccupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=1000)
    
    

    def __str__(self):
        return f"{self.name} ({self.type})"
    
class RoomImage(models.Model):
    image = models.ImageField(upload_to='room_images/')
    #image = CloudinaryField("image")
    caption = models.CharField(max_length=255, blank=True, null=True)
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Image for {self.room.name} - {self.caption or 'No Caption'}"

class OccupiedDate(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='occupiedDates')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='booked_dates')
    date = models.DateField()

    def __str__(self):
        return f"{self.date} - {self.room.name} booked by {self.user.username}"



class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100,default="")