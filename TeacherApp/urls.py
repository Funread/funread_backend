from django.urls import re_path
from TeacherApp import views

urlpatterns=[
    re_path(r'^teacher$',views.teacherApi),
    re_path(r'^teacher/([0-9]+)$', views.teacherApi)
]