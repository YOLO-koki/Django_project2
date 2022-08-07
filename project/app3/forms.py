from dataclasses import field
from pyexpat import model
from django import forms
from .models import Nutritions, Target

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
        labels = {
            'food': '食品',
            'calorie': 'カロリー',
            'protein': 'タンパク質',
            'carbohydrate': '炭水化物',
            'lipid': '脂質',
        }

class TargetForm(forms.ModelForm):
    
    class Meta:
        model = Target
        fields = ['target_calorie', 'target_protein', 'target_carbohydrate', 'target_lipid']
        widgets = {
            'target_calorie': forms.NumberInput(),
            'target_protein': forms.NumberInput(),
            'target_carbohydrate': forms.NumberInput(),
            'target_lipid': forms.NumberInput(),
        }
        labels = {
            'target_calorie': '目標カロリー',
            'target_protein': '目標タンパク質',
            'target_carbohydrate': '目標炭水化物',
            'target_lipid': '目標脂質',
        }