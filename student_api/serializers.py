from dataclasses import field, fields
from rest_framework import serializers
from student_api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=('username', 'password')