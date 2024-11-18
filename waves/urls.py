# waves/urls.py

from django.urls import path
from . import views

app_name = 'waves'  

urlpatterns = [
    path('<int:pk>/edit/', views.edit_wave, name='edit-wave'),  
    path('<int:pk>/delete/', views.delete_wave, name='delete-wave'),  
    
]
