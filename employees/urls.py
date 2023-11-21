from django.urls import path
from employees.views import (EmployeeCreateAPIView, EmployeeListAPIView, EmployeeRetrieveAPIView, EmployeeUpdateAPIView,
                             EmployeeDestroyAPIView)

from employees.apps import EmployeesConfig

app_name = EmployeesConfig.name

urlpatterns = [
    path('create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
    path("list/", EmployeeListAPIView.as_view(), name='employee_list'),
    path("detail/<int:pk>/", EmployeeRetrieveAPIView.as_view(), name='employee_detail'),
    path("update/<int:pk>/", EmployeeUpdateAPIView.as_view(), name='employee_update'),
    path("delete/<int:pk>/", EmployeeDestroyAPIView.as_view(), name='employee_delete'),
]
