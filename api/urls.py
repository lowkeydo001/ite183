from django.urls import path
from api.views import function_base_view

urlpatterns = [
    path('fbv-students/', function_base_view.studentView),
    path('fbv-student/<int:student_id>', function_base_view.student)
]