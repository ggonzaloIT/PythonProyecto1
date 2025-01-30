from django.urls import path
from . import views

urlpatterns = [
    path('alquiler/', views.PersonaCreateView.as_view(), name='alquiler_create'),
    path('libro/', views.LibroCreateView.as_view(), name='libro_create'),
    path('autor/', views.AutorCreateView.as_view(), name='autor_create'),
    path('search/', views.search_view, name='search'),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('blogposts/', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('blogposts/<int:pk>/', views.BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blogposts/create/', views.BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blogposts/<int:pk>/edit/', views.BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('blogposts/<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='blogpost_delete'),
]