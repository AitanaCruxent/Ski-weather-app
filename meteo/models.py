from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Resort(models.Model):     
    name = models.CharField(max_length = 64) 
    slug = models.SlugField(unique=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

    base_elevation = models.IntegerField()
    top_elevation = models.IntegerField()

    region = models.CharField(max_length=50)
    
    description = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
