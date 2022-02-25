from django.urls import re_path
from student_api import views

urlpatterns=[
    re_path(r'^student$',views.studentAPI),
    re_path(r'^student/([0-9]+)$', views.studentAPI)
]