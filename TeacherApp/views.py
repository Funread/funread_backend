from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TeacherApp.models import Teachers
from TeacherApp.serializers import TeacherSerializer

# Create your views here.

@csrf_exempt
def teacherApi(request, id=0):
    if request.method == 'GET':
        teachers = Teachers.objects.all()
        teachers_serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(teachers_serializer.data, safe=False)
    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        teachers_serializer = TeacherSerializer(data=teacher_data)
        if teachers_serializer.is_valid():
            teachers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        teacher_data = JSONParser().parse(request)
        teacher = Teachers.objects.get(TeacherId=teacher_data['TeacherId'])
        teachers_serializer = TeacherSerializer(teacher, data=teacher_data)
        if teachers_serializer.is_valid():
            teachers_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        teacher = Teachers.objects.get(TeacherId=id)
        teacher.delete()
        return JsonResponse("Deleted successfully", safe=False)
    


