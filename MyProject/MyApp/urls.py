from django.urls import path
from .views import index, food_sharing, nutrition_tracking
from .auth_views import register, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('food_sharing/', food_sharing, name='food_sharing'),
    path('nutrition_tracking/', nutrition_tracking, name='nutrition_tracking'),
    path('recipe_suggestion/', recipe_suggestion, name='recipe_suggestion'),
    path('meal_planner/', meal_planner, name='meal_planner'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
