from django.urls import path
from . import views

urlpatterns = [
    path('alquiler/', views.PersonaCreateView.as_view(), name='alquiler_create'),
    path('libro/', views.LibroCreateView.as_view(), name='libro_create'),
    path('autor/', views.AutorCreateView.as_view(), name='autor_create'),
    path('search/', views.search_view, name='search'),
]