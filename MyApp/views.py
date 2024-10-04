import urllib.request
import json
from django.shortcuts import render
from .models import FoodItem, Recipe, NutritionLog

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def food_sharing(request):
    return render(request, 'main/food_sharing.html')

def nutrition_tracking(request):
    return render(request, 'main/nutrition_tracking.html')

from django.shortcuts import render
from .food_api import get_nutrition_info

def recipe_suggestion(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients').split(',')
        # Logic to fetch and suggest recipes based on ingredients
        recipes = []  # Replace with actual recipe fetching logic
        return render(request, 'recipes.html', {'recipes': recipes})
    return render(request, 'recipe_suggestion.html')

def meal_planner(request):
    if request.method == 'POST':
        meal_date = request.POST['meal_date']
        meal_description = request.POST['meal_description']
        # Logic to save meal plan to the database
        return redirect('meal_planner')
    return render(request, 'meal_planner.html')


