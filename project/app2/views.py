from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import ConditionForm
from .models import Condition
from django.urls import reverse_lazy
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import datetime as dt


class ConditionCreateView(CreateView):
    # モデルを指定する
    model = Condition
    # フォームを指定する
    form_class = ConditionForm
    # テンプレートを指定する
    template_name = "app2/create.html"
    # フォーム送信完了後の遷移ページを指定する
    success_url = reverse_lazy("app2:index")

class ConditionUpdateView(UpdateView):
    model = Condition
    template_name = "app2/update.html"
    fields = ['height', 'weight', 'fat', 'waist']
    success_url = reverse_lazy('app2:index')

class ConditionDeleteView(DeleteView):
    model = Condition
    template_name = "app2/delete.html"
    success_url = reverse_lazy('app2:index')

class IndexView(ListView):
    template_name: str = 'app2/index.html'
    model = Condition
    context_object_name = 'conditions'
    paginate_by: int = 30

class ConditionGraphView(TemplateView):
    template_name = "app2/graph.html"
    
def getPlot(request):
    setPlt()
    svg = pltToSvg()
    plt.cla()
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

# グラフ作成
def setPlt():
    # 折れ線グラフを出力
    created_at_list = []
    for created_at in Condition.objects.values_list('created_at'):
        t = created_at[0]+dt.timedelta(hours=9)
        created_at_list.append(t)
    x = np.array(created_at_list)
    # x = np.array(Condition.objects.values_list('created_at'))
    y = np.array(Condition.objects.values_list('weight'))
    
    plt.figure(figsize=(20,10))
    plt.plot(x, y)
    plt.xlabel("time")
    plt.ylabel("weight")
    plt.show()


# SVG化
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s