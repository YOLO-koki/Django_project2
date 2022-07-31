from django.db import models
from django.utils import timezone

# Create your models here.
class Condition(models.Model):
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    fat = models.FloatField()
    waist = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __float__(self):
        return self.weight
    