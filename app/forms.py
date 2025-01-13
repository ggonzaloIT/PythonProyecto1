from django import forms
from .models import Persona, Libro, Autor

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)