from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from TeacherApp import views

urlpatterns=[
    # re_path(r'^teacher$',views.teacherApi),
    # re_path(r'^teacher/([0-9]+)$', views.teacherApi)
    path('', views.teacher_list),
    path('<int:pk>/', views.teacher_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)