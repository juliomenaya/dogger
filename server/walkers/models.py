from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

DAY_CHOICES = (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday')
)

class Walkers(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='walker')

    def __str__ (self):
        return f'{self.name} {self.last_name}'


class Schedules(models.Model):
    day_of_week = models.CharField(max_length=10, default='Monday', choices=DAY_CHOICES)
    hour = models.PositiveSmallIntegerField(validators=[MinValueValidator(7), MaxValueValidator(20)])
    size = models.ForeignKey('dogs.DogSize', null=True, blank=True, on_delete=models.SET_NULL)
    walker = models.ForeignKey(Walkers, related_name='schedules', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day_of_week} at {self.hour}'


class ScheduledWalks(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    dog = models.ForeignKey('dogs.Dogs', on_delete=models.CASCADE, related_name='walks')
    walker = models.ForeignKey(Walkers, on_delete=models.CASCADE, related_name='walks')
    date = models.DateField()
    day = models.CharField(max_length=10, default='Monday', choices=DAY_CHOICES)
    hour = models.PositiveSmallIntegerField(validators=[MinValueValidator(7), MaxValueValidator(20)])

    def __str__(self):
        return  f'{self.walker.name} with {self.dog.name}'
