from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Resort(models.Model):     
    name = models.CharField(max_length = 64) 
    slug = models.SlugField(unique=True)

    base_elevation = models.IntegerField()
    top_elevation = models.IntegerField()

    base_lat = models.DecimalField(max_digits=9, decimal_places=6)
    base_lon = models.DecimalField(max_digits=9, decimal_places=6)

    top_lat = models.DecimalField(max_digits=9, decimal_places=6)
    top_lon = models.DecimalField(max_digits=9, decimal_places=6)

    region = models.CharField(max_length=50)
    
    description = models.TextField()

    def __str__(self):
        return self.name



class Summit(models.Model):     
    name = models.CharField(max_length = 64) 
    slug = models.SlugField(unique=True)

    top_elevation = models.IntegerField()

    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    region = models.CharField(max_length=50)
    
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Route(models.Model): 

    LOCATION_CHOICES = [
    ('Val dAran', 'Val dAran'),
    ('Pallars', 'Pallars'),
    ('Alta Ribagorça', 'Alta Ribagorça'),
    ('Cerdanya', 'Cerdanya'), 
    ('Ripollés', 'Ripollés'),
    ('Pirineus', 'Pirineus'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length =64, choices=LOCATION_CHOICES, default='Pirineus')
    weather_info = models.TextField(max_length=100, blank=True, null=True)
    distance_km = models.DecimalField(max_digits= 6, decimal_places= 2, null=True, blank=True)
    duration_hours = models.PositiveIntegerField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    date_completed = models.DateField(blank=True, null= True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.name} owned by {self.owner}"