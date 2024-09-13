from django import forms
from .models import InputData

class InputDataForm(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['id', 'stockCode', 'companyName', 'industry', 'sector', 'website', 'about', 'singleLine', 'upTrend', 'downTrend', 'lineTouch', 'lineCross']