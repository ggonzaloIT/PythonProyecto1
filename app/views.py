from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import Modelo1Form, Modelo2Form, Modelo3Form, SearchForm
from .models import Model1, Model2, Model3

class Model1CreateView(CreateView):
    model = Model1
    form_class = Modelo1Form
    template_name = 'app/model1_form.html'
    success_url = '/model1/'

class Model2CreateView(CreateView):
    model = Model2
    form_class = Modelo2Form
    template_name = 'app/model2_form.html'
    success_url = '/model2/'

class Model3CreateView(CreateView):
    model = Model3
    form_class = Modelo3Form
    template_name = 'app/model3_form.html'
    success_url = '/model3/'

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_model1 = Model1.objects.filter(nombre__icontains=query)
            results_model2 = Model2.objects.filter(titulo__icontains=query)
            results_model3 = Model3.objects.filter(autor__icontains=query)
            results = list(results_model1) + list(results_model2) + list(results_model3)
            return render(request, 'app/search_results.html', {'form': form, 'results': results})
    else:
        form = SearchForm()
    return render(request, 'app/search_form.html', {'form': form})