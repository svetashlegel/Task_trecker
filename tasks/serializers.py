from rest_framework import serializers

from tasks.models import Task
from tasks.services import get_suitable_employee


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class ImportantTaskSerializer(serializers.ModelSerializer):
    available_employee = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'deadline', 'available_employee']

    def get_available_employee(self, obj):
        """Реализует поиск сотрудников джля выполнения важных задач"""
        available_emp = []
        base_task_executor = obj.base_task.executor
        employee = get_suitable_employee(base_task_executor)
        res = f'{employee.first_name} {employee.second_name} - {employee.position}'
        available_emp.append(res)
        return available_emp
