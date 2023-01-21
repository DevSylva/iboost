from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=522)
    username = models.CharField(unique=True, max_length=30)
    mobile_number = PhoneNumberField(default="", null=True, blank=True)
    balance = models.FloatField(default=0.0)
    address = models.TextField(default="", null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    zipcode = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    profile_pic = models.ImageField(default="", null=True, blank=True)

    def __str__(self):
        return self.email