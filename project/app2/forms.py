from django import forms
from .models import Condition

class ConditionForm(forms.ModelForm):
    
    class Meta:
        # どのモデルを利用するのか
        model = Condition
        # 表示させるフィールド
        fields = ['height', 'weight', 'fat', 'waist']
        widgets = {
            'height': forms.NumberInput(),
            'weight': forms.NumberInput(),
            'fat': forms.NumberInput(),
            'waist': forms.NumberInput(),
        }
        label = {
            'height': '身長',
            'weight': '体重',
            'fat': '体脂肪率',
            'waist': '腹囲',
        }