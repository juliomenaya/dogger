from django.db import models
from users.models import Users


class Dogs(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    size = models.ForeignKey('DogSize', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    # dog will have a walker just when his owner scheduled a walk
    # walker = models.ForeignKey('walkers.Walkers', on_delete=models.CASCADE, null=True, blank=True)

    def __str__ (self):
        return self.name


class DogSize(models.Model):
    size = models.CharField(max_length=8)

    def __str__ (self):
        return self.size

