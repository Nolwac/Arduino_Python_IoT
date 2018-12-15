from django.contrib import admin
from .models import Device

admin.site.register(Device) #this is to enable us create and view a device from the built-in Admin page
