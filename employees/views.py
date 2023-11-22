from rest_framework import generics
from django.db.models import Prefetch, Case, When, IntegerField, Sum

from employees.models import Employee
from employees.serializers import EmployeeSerializer
from tasks.models import Task


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
    queryset = (Employee.objects.filter(task__isnull=False).annotate(task_count=Sum(Case(When(task__is_completed=False,
                then=1), default=0, output_field=IntegerField()))).order_by('-task_count').prefetch_related(Prefetch(
        'task_set', queryset=Task.objects.filter(is_completed=False))))
