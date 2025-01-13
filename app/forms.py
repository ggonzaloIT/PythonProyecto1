from django import forms
from .models import Model1, Model2, Model3

class Modelo1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = '__all__'

class Modelo2Form(forms.ModelForm):
    class Meta:
        model = Model2
        fields = '__all__'

class Modelo3Form(forms.ModelForm):
    class Meta:
        model = Model3
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)