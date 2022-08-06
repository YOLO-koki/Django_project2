from django.urls import path
from .views import ConditionCreateView, IndexView, ConditionUpdateView, ConditionDeleteView, ConditionGraphView
from . import views

app_name = 'app2'
urlpatterns = [
    path('create/', ConditionCreateView.as_view(), name='create_condition'),
    path('update/<int:pk>/', ConditionUpdateView.as_view(), name='update_condition'),
    path('delete/<int:pk>/', ConditionDeleteView.as_view(), name='delete_condition'),
    path('index/', IndexView.as_view(), name='index'),
    path('graph/', ConditionGraphView.as_view(), name='graph'),
    path('plot/', views.getPlot, name='plot'),
]