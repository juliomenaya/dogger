from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Dogs(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    size = models.ForeignKey('DogSize', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey('Users', on_delete=models.CASCADE)
    walker = models.ForeignKey('Walkers', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__ (self):
        return self.name

class DogSize(models.Model):
    size = models.CharField(max_length=8)

    def __str__ (self):
        return self.size

class Schedules(models.Model):
    day_of_week = models.CharField(max_length=10, default='Monday',
        choices=(('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday'),
            ('saturday', 'Saturday'),
            ('sunday', 'Sunday')))
    hour = models.PositiveSmallIntegerField(validators=[MinValueValidator(7), MaxValueValidator(20)])
    size = models.ForeignKey('DogSize', null=True, blank=True, on_delete=models.SET_NULL)
