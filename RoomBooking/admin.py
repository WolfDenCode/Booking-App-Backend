from django.contrib import admin
from .models import User

from .models import Room,OccupiedDate
# Register your models here.

admin.site.register(Room)
admin.site.register(User)
admin.site.register(OccupiedDate)
