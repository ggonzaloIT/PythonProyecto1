from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox_view, name='inbox'),
    path('sent/', views.sent_view, name='sent'),
    path('send/', views.send_message_view, name='send_message'),
]