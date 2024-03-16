# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    imageUrl = models.ImageField(default="images/defaultAvatar.png" , upload_to="images/")
    def __str__(self):
        return self.username