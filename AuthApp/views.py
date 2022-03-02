# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login_view(request):

  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)

  if user is not None:
    login(request, user)
    # just temporary; use rest framework to get correct status code later
    return HttpResponse('<h1>Login Success</h1>')
  else:
    # just temporary; change this to 401 error later (using rest framework)
    return HttpResponseNotFound('<h1>Login failed</h1>')

@csrf_exempt
def logout_view(request):
  logout(request)
  
 
