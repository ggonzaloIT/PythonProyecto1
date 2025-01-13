from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import PersonaForm, LibroForm, AutorForm, SearchForm
from .models import Persona, Libro, Autor

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'app/alquiler_form.html'
    success_url = '/alquiler/'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'app/libro_form.html'
    success_url = '/libro/'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'app/autor_form.html'
    success_url = '/autor/'

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_persona = Persona.objects.filter(nombre__icontains=query)
            results_libro = Libro.objects.filter(titulo__icontains=query)
            results_autor = Autor.objects.filter(autor__icontains=query)
            results = list(results_persona) + list(results_libro) + list(results_autor)
            return render(request, 'app/search_results.html', {'form': form, 'results': results})
    else:
        form = SearchForm()
    return render(request, 'app/search_form.html', {'form': form})