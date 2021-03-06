from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name