from django.urls import path, include
from api.views import student_function_base_view
from api.views import employee_function_base_view
from api.views import student_class_base_view
from api.views import employee_class_base_view
from api.views import mixins_employee
from api.views import mixins_student 
from api.views import generics_employee
from api.views import generics_student
from rest_framework.routers import DefaultRouter
import api.views.employee_viewsets as viewsets_view
import api.views.student_viewsets as student_viewsets

router = DefaultRouter()
router.register('viewsets-employees', viewsets_view.Employees, basename='viewsets-employees')
router.register('model-viewsets-employees', viewsets_view.EmployeeModelViewSet)

router.register('viewsets-students', student_viewsets.Students, basename='viewsets-students')
router.register('model-viewsets-students', student_viewsets.StudentModelViewSet)



urlpatterns = [
    path('fbv-students/', student_function_base_view.studentView),
    path('fbv-students/<int:student_id>/', student_function_base_view.student),

    path('fbv-employees/', employee_function_base_view.EmployeeView),
    path('fbv-employees/<int:employee_id>/', employee_function_base_view.employee),

    path('cbv-students/', student_class_base_view.Students.as_view()),
    path('cbv-student_detail/<int:pk>/', student_class_base_view.StudentDetail.as_view()),

    path('cbv-employees/', employee_class_base_view.Employees.as_view()),
    path('cbv-employee/<int:pk>/', employee_class_base_view.EmployeeDetail.as_view()),

    path('mixins_employees/', mixins_employee.Employees.as_view()),
    path('mixins-employees-detail/<int:pk>/', mixins_employee.EmployeeDetail.as_view()),

    path('mixins_students/', mixins_student.Students.as_view()),
    path('mixins-students-detail/<int:pk>/', mixins_student.StudentDetail.as_view()),

    path('generics_employee/', generics_employee.Employees.as_view()),
    path('generics-employee-detail/<int:pk>/', generics_employee.EmployeeDetail.as_view()),
     
    path('generics-students/', generics_student.Students.as_view()), 
    path('generics-students/<int:pk>/', generics_student.StudentDetail.as_view()), 

    path('', include(router.urls))

]
    