from rest_framework import generics

from tasks.models import Task
from tasks.serializers import TaskSerializer, ImportantTaskSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()


class ImportantTaskListAPIView(generics.ListAPIView):
    """
    Выводит список важных задач и возможных сотрудников для их выполнения.
    Важные задачи - задачи, не взятые в работу, и от которых зависят другие
    задачи, взятые в работу.
    """

    serializer_class = ImportantTaskSerializer
    queryset = Task.objects.filter(executor__isnull=True, base_task__isnull=False, base_task__executor__isnull=False)
