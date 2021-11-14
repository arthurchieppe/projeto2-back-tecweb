from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    cities = ArrayField(models.CharField(max_length=40, blank=False))
    

    def __str__(self):
      return f"{self.tagTitle}"

