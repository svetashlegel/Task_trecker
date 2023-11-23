from rest_framework import generics
from django.db.models import Prefetch, Case, When, IntegerField, Sum

from employees.models import Employee
from employees.serializers import EmployeeSerializer
from tasks.models import Task


class EmployeeCreateAPIView(generics.CreateAPIView):
    """Создание сотрудника."""
    serializer_class = EmployeeSerializer


class EmployeeListAPIView(generics.ListAPIView):
    """Общий список сотрудников."""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одного сотрудника."""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о сотруднике."""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyAPIView(generics.DestroyAPIView):
    """Удаление сотрудника."""
    queryset = Employee.objects.all()


class EngagedEmployeesListAPIView(generics.ListAPIView):
    """Список занятых сотрудников, отсортированные по количеству активных задач."""
    serializer_class = EmployeeSerializer
    queryset = (Employee.objects.filter(task__isnull=False).annotate(task_count=Sum(Case(When(task__is_completed=False,
                then=1), default=0, output_field=IntegerField()))).order_by('-task_count').prefetch_related(Prefetch(
        'task_set', queryset=Task.objects.filter(is_completed=False))))
