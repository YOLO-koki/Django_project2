from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Nutritions
from .forms import NutritionsForm
from django.urls import reverse_lazy

# Create your views here.
class Nutrition(TemplateView):
    template_name: str = 'app3/nutritions.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nutritions"] = Nutritions.objects.all()
        return context

class NutritionsCreateView(CreateView):
    model = Nutritions
    template_name = "app3/create.html"
    form_class = NutritionsForm
    success_url = reverse_lazy('app3:nutrition')

    