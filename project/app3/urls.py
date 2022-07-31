from django.urls import path
from .views import Nutrition, NutritionsCreateView

app_name = 'app3'
urlpatterns = [
    path('', Nutrition.as_view(), name='nutrition'),
    path('create/', NutritionsCreateView.as_view(), name='create_nutrition'),
]