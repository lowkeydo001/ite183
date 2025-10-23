from rest_framework import generics
from students.models import Student
from api.serializer import StudentSerializer

class Students(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Option 2
class Students(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'pk'

# Option 2
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
