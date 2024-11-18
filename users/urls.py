from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('@me/', views.my_user_detail, name='my_user_detail'),
    path('<str:username>/', views.user_profile, name='user-profile'),
    path('<str:username>/echos/', views.user_echos, name='user-echos'),
    path('<str:username>/edit/', views.edit_user, name='edit-user'),
]
