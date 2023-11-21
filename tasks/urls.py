from django.urls import path
from tasks.views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView

from tasks.apps import TasksConfig

app_name = TasksConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task_create'),
    path("list/", TaskListAPIView.as_view(), name='task_list'),
    path("detail/<int:pk>/", TaskRetrieveAPIView.as_view(), name='task_detail'),
    path("update/<int:pk>/", TaskUpdateAPIView.as_view(), name='task_update'),
    path("delete/<int:pk>/", TaskDestroyAPIView.as_view(), name='task_delete'),
]
