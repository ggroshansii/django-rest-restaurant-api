from django.db import models

# Create your models here.

class OrderItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25)
    tax = models.FloatField()
    total = models.FloatField()
    isCompleted = models.BooleanField()
    order = models.JSONField()

    def __str__(self):
        return self.order