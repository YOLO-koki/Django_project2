from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Nutritions, Target
from .forms import NutritionsForm, TargetForm
from django.urls import reverse_lazy

# Create your views here.
class Nutrition(TemplateView):
    template_name: str = 'app3/nutritions.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if len(Target.objects.all()) > 0 and len(Nutritions.objects.all()) > 0:
            # 入力値の取得
            context["nutritions"] = Nutritions.objects.all()
            
            # 各値の合計値
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
            
            context["target_id"] = Target.objects.values_list('id')[len(Target.objects.values_list('id'))-1][0]
            
            # 目標の取得(データの一番後ろのデータを取得) ※更新しているわけではない
            context["target_calorie"] = Target.objects.values_list('target_calorie')[len(Target.objects.values_list('target_calorie'))-1][0]
            context["target_protein"] = Target.objects.values_list('target_protein')[len(Target.objects.values_list('target_protein'))-1][0]
            context["target_carbohydrate"] = Target.objects.values_list('target_carbohydrate')[len(Target.objects.values_list('target_carbohydrate'))-1][0]
            context["target_lipid"] = Target.objects.values_list('target_lipid')[len(Target.objects.values_list('target_lipid'))-1][0]
        
            # 目標値と入力値の差
            context["sub_calorie"] =  context["sum_calorie"] - context["target_calorie"]
            context["sub_protein"] =  context["sum_protein"] - context["target_protein"]
            context["sub_carbohydrate"] = context["sum_carbohydrate"] - context["target_carbohydrate"]
            context["sub_lipid"] = context["sum_lipid"] - context["target_lipid"]
            
            return context
        
        # Nutritionsにデータが入っていた場合
        elif len(Nutritions.objects.all()) > 0:
            # 入力値の取得
            context["nutritions"] = Nutritions.objects.all()
            
            # 各値の合計値
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
        
        # Targetにデータが入っていた場合
        elif len(Target.objects.all()) > 0:
            context["target_id"] = Target.objects.values_list('id')[len(Target.objects.values_list('id'))-1][0]
            
            # 目標の取得(データの一番後ろのデータを取得) ※更新しているわけではない
            context["target_calorie"] = Target.objects.values_list('target_calorie')[len(Target.objects.values_list('target_calorie'))-1][0]
            context["target_protein"] = Target.objects.values_list('target_protein')[len(Target.objects.values_list('target_protein'))-1][0]
            context["target_carbohydrate"] = Target.objects.values_list('target_carbohydrate')[len(Target.objects.values_list('target_carbohydrate'))-1][0]
            context["target_lipid"] = Target.objects.values_list('target_lipid')[len(Target.objects.values_list('target_lipid'))-1][0]
            
            return context
        
        # Nutritions または Target にデータが入っていなかった場合
        else:
            context["sum_calorie"] = 0
            context["sum_protein"] = 0
            context["sum_carbohydrate"] = 0
            context["sum_lipid"] = 0
            
            # 目標の取得(データの一番後ろのデータを取得) ※更新しているわけではない
            context["target_calorie"] = 0
            context["target_protein"] = 0
            context["target_carbohydrate"] = 0
            context["target_lipid"] = 0
            
            # 目標値と入力値の差
            context["sub_calorie"] =  0
            context["sub_protein"] =  0
            context["sub_carbohydrate"] = 0
            context["sub_lipid"] = 0
            
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

# 目標値 設定
class TargetCreateView(CreateView):
    model = Target
    form_class = TargetForm
    template_name = "app3/create_target.html"
    success_url = reverse_lazy('app3:nutrition')
    
class TargetUpdateView(UpdateView):
    model = Target
    template_name = "app3/update_target.html"
    fields = ['target_calorie', 'target_protein', 'target_carbohydrate', 'target_lipid']
    success_url = reverse_lazy('app3:nutrition')

# リセット
def reset(request):
    Target.objects.all().delete()
    Nutritions.objects.all().delete()
    context = {}
    context["sum_calorie"] = 0
    context["sum_protein"] = 0
    context["sum_carbohydrate"] = 0
    context["sum_lipid"] = 0
    
    # 目標の取得(データの一番後ろのデータを取得) ※更新しているわけではない
    context["target_calorie"] = 0
    context["target_protein"] = 0
    context["target_carbohydrate"] = 0
    context["target_lipid"] = 0
    
    # 目標値と入力値の差
    context["sub_calorie"] =  0
    context["sub_protein"] =  0
    context["sub_carbohydrate"] = 0
    context["sub_lipid"] = 0
    
    return render(request, 'app3/nutritions.html', context)