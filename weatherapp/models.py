from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
    # id = models.AutoField()
    username = models.CharField(max_length=200, primary_key=True)
    cities = ArrayField(models.CharField(max_length=40), blank=True, default=['São Paulo'])
    

    def __str__(self):
      return f"{self.tagTitle}"

