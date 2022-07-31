import imp
from django.urls import path
from .views import StartView

app_name = 'app1'
urlpatterns = [
    path('', StartView.as_view(), name='start'),
]
