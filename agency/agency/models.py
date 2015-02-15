from django.db import models

# Create your models here.

class Location(models.Model):
    zip = models.IntegerField(max_length = 5)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 2)
    street = models.CharField(max_length = 200)
