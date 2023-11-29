from rest_framework import generics

from tasks.models import Task
from tasks.serializers import TaskSerializer, ImportantTaskSerializer
from tasks.paginators import TasksPaginator


class TaskCreateAPIView(generics.CreateAPIView):
    """Создание задачи."""
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    """Общий список задач."""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    pagination_class = TasksPaginator


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одной задачи."""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    """Обновление задачи."""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(generics.DestroyAPIView):
    """Удаление задачи."""
    queryset = Task.objects.all()


class ImportantTaskListAPIView(generics.ListAPIView):
    """
    Список важных задач и возможных сотрудников для их выполнения.
    Важные задачи - задачи, не взятые в работу, и от которых зависят
    другие задачи, взятые в работу.
    """

    serializer_class = ImportantTaskSerializer
    queryset = Task.objects.filter(executor__isnull=True, base_task__isnull=False, base_task__executor__isnull=False)
    pagination_class = TasksPaginator
