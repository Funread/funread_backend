from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TeacherApp.models import Teachers
from TeacherApp.serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# @csrf_exempt
# def teacherApi(request, id=0):
#     if request.method == 'GET':
#         teachers = Teachers.objects.all()
#         teachers_serializer = TeacherSerializer(teachers, many=True)
#         return JsonResponse(teachers_serializer.data, safe=False)
#     elif request.method == 'POST':
#         teacher_data = JSONParser().parse(request)
#         teachers_serializer = TeacherSerializer(data=teacher_data)
#         if teachers_serializer.is_valid():
#             teachers_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method == 'PUT':
#         teacher_data = JSONParser().parse(request)
#         teacher = Teachers.objects.get(TeacherId=teacher_data['TeacherId'])
#         teachers_serializer = TeacherSerializer(teacher, data=teacher_data)
#         if teachers_serializer.is_valid():
#             teachers_serializer.save()
#             return JsonResponse("Update Successfully", safe=False)
#         return JsonResponse("Failed to Update", safe=False)
#     elif request.method == 'DELETE':
#         teacher = Teachers.objects.get(TeacherId=id)
#         teacher.delete()
#         return JsonResponse("Deleted successfully", safe=False)

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
    


