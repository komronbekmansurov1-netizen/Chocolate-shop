from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'customer', 'Haridor'
        ADMIN = 'admin', 'Admin'
    role = models.CharField(max_length=100, choices=Role.choices)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)    
    address = models.CharField(max_length=255)
    passport_seria = models.CharField(max_length=100)
    passport_image = models.ImageField(upload_to='passport_image/', blank=True, null=True)

    def __str__(self):
        return self.name