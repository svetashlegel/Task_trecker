from rest_framework import serializers

from employees.models import Employee
from tasks.serializers import TaskSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(source='task_set', many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        