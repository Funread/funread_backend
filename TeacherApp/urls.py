from unicodedata import name
from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from TeacherApp import views

urlpatterns=[

    path('', views.teacher_list),
    path('<int:pk>/', views.teacher_detail),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)