from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Nutritions
from .forms import NutritionsForm
from django.urls import reverse_lazy

# Create your views here.
class Nutrition(TemplateView):
    template_name: str = 'app3/nutritions.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nutritions"] = Nutritions.objects.all()
        sum_calorie = []
        sum_protein = []
        sum_carbohydrate = []
        sum_lipid = []
        for i in range(len((Nutritions.objects.values_list('calorie')))):
            sum_calorie.append(Nutritions.objects.values_list('calorie')[i][0])
            sum_protein.append(Nutritions.objects.values_list('protein')[i][0])
            sum_carbohydrate.append(Nutritions.objects.values_list('carbohydrate')[i][0])
            sum_lipid.append(Nutritions.objects.values_list('lipid')[i][0])
        context["sum_calorie"] = sum(sum_calorie)
        context["sum_protein"] = sum(sum_protein)
        context["sum_carbohydrate"] = sum(sum_carbohydrate)
        context["sum_lipid"] = sum(sum_lipid)
        return context
    

class NutritionsCreateView(CreateView):
    model = Nutritions
    template_name = "app3/create.html"
    form_class = NutritionsForm
    success_url = reverse_lazy('app3:nutrition')

class NutritionsUpdateView(UpdateView):
    model = Nutritions
    template_name = "app3/update.html"
    fields = ['food', 'calorie', 'protein', 'carbohydrate', 'lipid']
    success_url = reverse_lazy('app3:nutrition')

class NutritionsDeleteView(DeleteView):
    model = Nutritions
    template_name = "app3/delete.html"
    success_url = reverse_lazy('app3:nutrition')
