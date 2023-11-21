from rest_framework import generics
from django.db.models import Count

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeCreateAPIView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()


class EngagedEmployeesListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(task__isnull=False).annotate(task_count=Count('task')).order_by('-task_count')
