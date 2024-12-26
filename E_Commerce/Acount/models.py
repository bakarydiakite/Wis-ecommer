from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    confirm_pwd = models.CharField(max_length=32)
    