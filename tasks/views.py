from rest_framework import generics

from tasks.models import Task
from tasks.serializers import TaskSerializer


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
