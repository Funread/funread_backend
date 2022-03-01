import imp
from multiprocessing import managers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from student_api.models import Student
from student_api.serializers import StudentSerializer


# Create your views here.

@csrf_exempt
def studentAPI(request, id=0):
    if request.method=='GET':
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
    elif request.method=='POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        print("Marker: In PUT")
        student_data = JSONParser().parse(request)
        print("student_id: " + str(student_data['student_id']))
        student = Student.objects.get(student_id=student_data['student_id'])
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        student = Student.objects.get(student_id=id)
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)

        
