from django.urls import path
from django.contrib.auth import views as auth_views
from AuthApp import views

urlpatterns = [
  path('login/', views.login_view, name='login')
  
]