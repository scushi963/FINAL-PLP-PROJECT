from django.db import models
from django.contrib.auth.models import User

# Food item model to store food details
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    nutritional_info = models.JSONField()  # Storing nutritional details like calories, protein, etc. in JSON format

    def __str__(self):
        return self.name

# Recipe model to store recipe details and related food items
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(FoodItem)  # Many-to-Many relation as multiple food items can be part of a recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Recipe created by a user

    def __str__(self):
        return self.title

# Nutrition Log to track food intake by the user
class NutritionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each log is associated with a user
    date = models.DateField()
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # Logs the food item consumed
    quantity = models.FloatField()  # Stores the quantity of the food item consumed

    def __str__(self):
        return f'{self.user.username} - {self.food_item.name} on {self.date}'

