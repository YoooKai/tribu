# accounts/urls.py
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.user_signup, name='user-signup'),
]
