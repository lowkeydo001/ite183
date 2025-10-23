from django.shortcuts import render, get_object_or_404  
from students.models import Student
from api.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET', 'POST'])
def studentView(request, pk=None):
    if pk is None:
        if(request.method == 'GET'):
           # Get all the data from the student table
           students = Student.objects.all()
           serializer = StudentSerializer(students, many=True)
           print (students, serializer.data)
           return Response(serializer.data, status=status.HTTP_200_OK)

        if(request.method == 'POST'):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)