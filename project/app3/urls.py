from django.urls import path
from .views import Nutrition, NutritionsCreateView, NutritionsUpdateView, NutritionsDeleteView

app_name = 'app3'
urlpatterns = [
    path('', Nutrition.as_view(), name='nutrition'),
    path('create/', NutritionsCreateView.as_view(), name='create_nutrition'),
    path('update/<int:pk>', NutritionsUpdateView.as_view(), name='update_nutrition'),
    path('delete/<int:pk>', NutritionsDeleteView.as_view(), name='delete_nutrition'),
]