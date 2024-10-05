import urllib.request
import json
from django.shortcuts import render, redirect
from .models import FoodItem, Recipe, NutritionLog
from django.contrib.auth import login, authenticate
from .forms import FoodSharingForm, NutritionLogForm, CommunityEngagementForm

# Create your views here.
def index(request):
    # Handle food sharing form submission
    if request.method == 'POST' and 'food_sharing' in request.POST:
        food_form = FoodSharingForm(request.POST)
        if food_form.is_valid():
            food_form.save()
            # Optionally, redirect or render with a success message
    else:
        food_form = FoodSharingForm()

    # Handle nutrition log form submission
    if request.method == 'POST' and 'nutrition_log' in request.POST:
        nutrition_form = NutritionLogForm(request.POST)
        if nutrition_form.is_valid():
            nutrition_form.save()
            # Optionally, redirect or render with a success message
    else:
        nutrition_form = NutritionLogForm()

    # Handle community engagement form submission
    if request.method == 'POST' and 'community_engagement' in request.POST:
        engagement_form = CommunityEngagementForm(request.POST)
        if engagement_form.is_valid():
            engagement_form.save()
            # Optionally, redirect or render with a success message
    else:
        engagement_form = CommunityEngagementForm()

    context = {
        'food_form': food_form,
        'nutrition_form': nutrition_form,
        'engagement_form': engagement_form,
    }

    return render(request, 'main/index.html', context)

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
