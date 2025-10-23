from ..serializer import StudentSerializer
from rest_framework.response import Response 
from rest_framework import status #if e return ang data makabalo sa status sa response 
from rest_framework.views import APIView 
from students.models import Student
from django.http import Http404

# Class Base View
class Students(APIView):
    def get(self, request): # Request - kung unsa ang data sa frontend,ayha ra maggamit ang request pag mag post
        students = Student.objects.all() # E fetch ang data sa tanan students
        serializer = StudentSerializer(students, many=True) #Para ang data nga gi return sa student.objects.all (data) convert into json.. Ang gi serialize nga data E response sa client dayon
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request): #request mag handle sa data nga gi ano sa client
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #e save ang data sa database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)