from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Custom fields for e-commerce
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    shipping_address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True, related_name='shipping_users')
    billing_address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True, related_name='billing_users')

class Address(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    