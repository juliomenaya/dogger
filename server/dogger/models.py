from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Users(models.Models):
    name = models.CharField(max_Length=30)
    last_name = models.CharField(max_Length=30)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    walker = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    avatar = models.ImageField()
    timestamp = models.DataTimeField(auto_now_add=True, auto_now=False)

    def __str__ (self):
        return self.email

class Dogs(models.Models):
    name = models.CharField(max_Length=50)
    age = models.IntegerField()
    size = models.ForeignKey('DogSize', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey('Users', on_delete=models.CASCADE)
    walker = models.ForeignKey('Users', null=True, blank=True, on_delete=models.SET_NULL)
    schedule = models.JSONField(null=True, blank=True)

class DogSize(models.Models):
    size = models.CharFiel(max_Length=8)

class Schedules(models.Models):
    day_of_week = models.CharField(default='Monday',
        choices=(('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday'),
            ('saturday', 'Saturday'),
            ('sunday', 'Sunday')))
    hour = models.PositiveSmallIntegerField(validators=[MaxValueValidator(24)])
    dogs = models.ManyToManyField('Dogs', null=True, blank=True, on_delete=models.SET_NULL)

class Walkers(models.Models):
    walker = models.ForeignKey('Users', on_delete=models.CASCADE)
    schedules = models.ManyToManyField('Schedules', on_delete=models.DO_NOTHING)