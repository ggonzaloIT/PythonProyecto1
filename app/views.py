from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PersonaForm, LibroForm, AutorForm, SearchForm
from .models import Persona, Libro, Autor, BlogPost
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['titulo', 'autor', 'contenido', 'imagen', 'fecha_publicacion']
    template_name = 'app/blogpost_form.html'
    success_url = reverse_lazy('app:blogpost_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['titulo', 'autor', 'contenido', 'imagen', 'fecha_publicacion']
    template_name = 'app/blogpost_form.html'
    success_url = reverse_lazy('app:blogpost_list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'app/blogpost_confirm_delete.html'
    success_url = reverse_lazy('app:blogpost_list')
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'app/blogpost_detail.html'
    context_object_name = 'blogpost'

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'app/blogpost_list.html'
    context_object_name = 'blogposts'

    def get_queryset(self):
        return BlogPost.objects.all()
        


class PersonaCreateView(LoginRequiredMixin,CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'app/alquiler_form.html'
    success_url = '/alquiler/'

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)


class LibroCreateView(LoginRequiredMixin,CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'app/libro_form.html'
    success_url = '/libro/'

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)

class AutorCreateView(LoginRequiredMixin,CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'app/autor_form.html'
    success_url = '/autor/'

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)

@login_required
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

def home_view(request):
    return render(request, 'app/home.html')

def about_view(request):
    return render(request, 'app/about.html')