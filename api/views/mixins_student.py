from ..serializer import StudentSerializer
from rest_framework import mixins, generics
from students.models import Student


# 👉 Class nga mag-handle sa list ug create operations sa students gamit ang mixins ug generic API view
class Students(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()  # 👉 Kuhaon tanan Student records gikan sa database
    serializer_class = StudentSerializer  # 👉 Gamiton ang serializer para sa pag-convert sa data

    # 👉 Kung moabot ang GET request, i-return niya ang listahan sa tanang students
    def get(self, request):
        return self.list(request)  # 👉 ListModelMixin method para i-retrieve ang tanang records

    # 👉 Kung moabot ang POST request, mo-create siya ug bag-ong student record
    def post(self, request):
        return self.create(request)  # 👉 CreateModelMixin method para mo-save sa bag-ong data sa database


# 👉 Class nga mag-handle sa retrieve (get specific student), update, ug delete operations sa student gamit mixins
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()  # 👉 Kuhaon tanan Student records gikan sa database
    serializer_class = StudentSerializer  # 👉 Gamiton ang serializer para sa pag-convert sa data

    # 👉 Kung GET request para sa specific student gamit ang primary key (pk)
    def get(self, request, pk):
        return self.retrieve(request, pk)  # 👉 RetrieveModelMixin method para makuha ang specific record

    # 👉 Kung PUT request para i-update ang student record gamit ang pk
    def put(self, request, pk):
        return self.update(request, pk)  # 👉 UpdateModelMixin method para i-update ang record sa database

    # 👉 Kung DELETE request para tangtangon ang student record gamit ang pk
    def delete(self, request, pk):
        return self.destroy(request, pk)  # 👉 DestroyModelMixin method para i-delete ang record sa database
