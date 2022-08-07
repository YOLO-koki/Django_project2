from django.db import models
from django.utils import timezone

# Create your models here.
class Nutritions(models.Model):
    food = models.CharField(max_length=100, blank=False, null=False)
    calorie = models.IntegerField(blank=False, null=False)
    protein = models.FloatField(blank=False, null=False)
    carbohydrate = models.FloatField(blank=False, null=False)
    lipid = models.FloatField(blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)

class Target(models.Model):
    target_calorie = models.IntegerField(blank=False, null=False)
    target_protein = models.FloatField(blank=False, null=False)
    target_carbohydrate = models.FloatField(blank=False, null=False)
    target_lipid = models.FloatField(blank=False, null=False)