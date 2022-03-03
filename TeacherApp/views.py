from django.http import HttpResponse
from TeacherApp.models import Teachers
from TeacherApp.serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
# Create your views here.

@api_view(['GET', 'POST'])
def teacher_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Teachers.objects.all()
        serializer = TeacherSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Teachers.objects.get(pk=pk)
    except Teachers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def home(request):
    if 'teacher' in request.session:
        current_teacher = request.session['teacher']
        param = {'current_teacher': current_teacher}
        return render(request, 'home.html', param) 
    else:
        return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        tName = request.POST.get('tName')
        tPwd = request.POST.get('tPwd')

        if Teachers.objects.filter(TeacherName=tName).count()>0:
            return HttpResponse('Teacher already exist.')
        else:
            teacher = Teachers(TeacherName=tName, TeacherPwd=tPwd)
            teacher.save()
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        tName = request.POST.get('tName')
        tPwd = request.POST.get('tPwd')

        check_teacher = Teachers.objects.filter(TeacherName=tName, TeacherPwd=tPwd)
        if check_teacher:
            request.session['teacher'] = tName
            return redirect('home')
        else:
            return HttpResponse('Please enter valid teacher name or password')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['teacher']
    except:
        return redirect('login')
    return redirect('login')

