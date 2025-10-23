from ..serializer import EmployeeSerializer
from rest_framework import mixins, generics
from employees.models import Employee


# 👉 Kini nga class-based view maoy mo-handle sa pag-list sa tanang employees ug sa pag-create og bag-ong employee.
# Gigamit niya ang DRF (Django Rest Framework) nga mga mixins aron mas sayon ang pag-implementar sa CRUD (Create, Read, Update, Delete) nga mga operasyon.
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()  # 👉 Mukuha ni sa tanang "Employee" records gikan sa database.
    serializer_class = EmployeeSerializer  # 👉 Gigamit aron i-convert ang data gikan sa Python objects ngadto sa JSON ug pabalik.

    # 👉 Mo-handle sa GET request: Ibalik ang listahan sa tanang employees.
    def get(self, request):
        return self.list(request)  # 👉 Gigamit ang built-in method sa ListModelMixin nga list() aron mo-retrieve sa data.

    # 👉 Mo-handle sa POST request: Mo-create ug bag-ong employee record.
    def post(self, request):
        return self.create(request)  # 👉 Gigamit ang built-in method sa CreateModelMixin nga create() aron mo-save sa data sa database.

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)