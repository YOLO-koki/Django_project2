from django.urls import path
from .views import Nutrition, NutritionsCreateView, NutritionsUpdateView, NutritionsDeleteView, TargetCreateView, TargetUpdateView
from . import views

app_name = 'app3'
urlpatterns = [
    path('nutrition/', Nutrition.as_view(), name='nutrition'),
    path('create/nutrition/', NutritionsCreateView.as_view(), name='create_nutrition'),
    path('create_target/', TargetCreateView.as_view(), name='create_target'),
    path('update_target/<int:pk>', TargetUpdateView.as_view(), name='update_target'),
    path('update/<int:pk>', NutritionsUpdateView.as_view(), name='update_nutrition'),
    path('delete/<int:pk>', NutritionsDeleteView.as_view(), name='delete_nutrition'),
    path('reset/nutrition/', views.reset, name='reset_nutrition'),
]