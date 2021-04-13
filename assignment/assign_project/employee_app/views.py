from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from employee_app.serializers import EmployeeSerializer
from employee_app.models import Employees

# Create your views here.

class ListEmployeeAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployeeAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class UpdateEmployeeAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployeeAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer