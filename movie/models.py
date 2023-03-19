from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    director = models.CharField(max_length=20)
    rating = models.CharField(max_length=3)
    def __str__(self):
        return self.name