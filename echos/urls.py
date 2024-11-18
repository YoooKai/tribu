# echos/urls.py
from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('<int:pk>/', views.echo_detail, name='echo-detail'),
    path('add/', views.add_echo, name='add-echo'),
    path('<int:pk>/edit/', views.edit_echo, name='edit-echo'),
    path('<int:pk>/delete/', views.delete_echo, name='delete-echo'),
    path('<int:pk>/waves/add/', views.add_wave, name='add-wave'),
    path('<int:pk>/waves/', views.wave_list, name='wave-list'),
]
