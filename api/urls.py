from django.urls import path
from api.views import function_base_view

urlpatterns = [
    path('fbv-students/', function_base_view.studentView)
]