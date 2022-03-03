from dataclasses import fields
from rest_framework import serializers
from TeacherApp.models import Teachers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields=('TeacherId', 'TeacherName', 'TeacherPwd')