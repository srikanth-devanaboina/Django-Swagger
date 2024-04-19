from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from app1.models import Student
from app1.serializers import CreateStudentSerializer, UpdateStudentSerializer


class StudentList(generics.GenericAPIView):
    def get(self, request):
        student_list = Student.objects.values("id", "name")
        return Response(student_list)
    

class CreateStudent(generics.GenericAPIView):
    serializer_class = CreateStudentSerializer

    def post(self, request):
        # Request payload data
        name = request.data['name']
        age = request.data['age']
        mobile = request.data['mobile_number']

        # Create query
        Student.objects.create(
            name = name,
            age = age,
            mobile_number = mobile
        )

        return Response("student created")
    

class UpdateStudent(generics.GenericAPIView):
    serializer_class = UpdateStudentSerializer
    
    def put(self, request):

        Student.objects.filter(id=request.data['id']).update(
            name = request.data['name'],
            age =request.data['age']
        )

        return Response("student updated.")
    

class DeleteStudent(generics.GenericAPIView):

    def delete(self, request, student_id):
        Student.objects.filter(id=student_id).delete()

        return Response("student deleted.")
