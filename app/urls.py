from django.urls import path
from . import views

urlpatterns = [
    path('model1/', views.Model1CreateView.as_view(), name='model1_create'),
    path('model2/', views.Model2CreateView.as_view(), name='model2_create'),
    path('model3/', views.Model3CreateView.as_view(), name='model3_create'),
    path('search/', views.search_view, name='search'),
]