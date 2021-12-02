from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='owner')
    scheduled_walks = models.ManyToManyField('walkers.Walkers', through='walkers.ScheduledWalks', blank=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'
