from django.urls import path
from .views import index, food_sharing, nutrition_tracking
from .auth_views import register, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('food_sharing/', food_sharing, name='food_sharing'),
    path('nutrition_tracking/', nutrition_tracking, name='nutrition_tracking'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
