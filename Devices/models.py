from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
	"""This is the model for the device to be controlled from the website"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	state = models.BooleanField(default=False)

# Create your models here.
