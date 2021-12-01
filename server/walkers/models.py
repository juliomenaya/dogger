from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Walkers(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)