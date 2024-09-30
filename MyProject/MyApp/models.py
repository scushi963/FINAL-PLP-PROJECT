from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    nutritional_info = models.JSONField()

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(FoodItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class NutritionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
