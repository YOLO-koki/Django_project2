from django import forms
from .models import Nutritions

class NutritionsForm(forms.ModelForm):
    
    class Meta:
        # どのモデルを利用するのか
        model = Nutritions
        # 表示させるフィールド
        fields = ['food', 'calorie', 'protein', 'carbohydrate', 'lipid']
        widgets = {
            'food': forms.TextInput(),
            'calorie': forms.NumberInput(),
            'protein': forms.NumberInput(),
            'carbohydrate': forms.NumberInput(),
            'lipid': forms.NumberInput(),
        }
        label = {
            'food': '食品',
            'calorie': 'カロリー',
            'protein': 'タンパク質',
            'carbohydrate': '炭水化物',
            'lipid': '脂質',
        }