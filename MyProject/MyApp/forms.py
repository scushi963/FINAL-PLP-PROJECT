from django import forms
from .models import FoodItem, Recipe, NutritionLog, Experience

# Form for FoodItem (for creating new food items)
class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'category', 'nutritional_info']

# Form for Recipe (for creating new recipes)
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'ingredients']

# Form for NutritionLog (for logging nutrition data)
class NutritionLogForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['date', 'food_item', 'quantity']

# Form for Experience (for sharing experiences)
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['name', 'email', 'experience']
