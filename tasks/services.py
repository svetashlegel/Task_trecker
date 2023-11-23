from employees.models import Employee
from tasks.funcs import count_active_tasks


def get_suitable_employee(base_task_executor):
    """
    Подбирает подходящего сотрудника для выполнения задачи.
    Подходящий сотрудник - сотрудник с наименьшей занятостью
    или сотрудник выполняющий родительскую задачу если ему
    назначено максимум на 2 задачи больше, чем у наименее
    загруженного сотрудника.
    """
    queryset = Employee.objects.all()
    not_busy_employee = Employee.objects.all().first()
    min_tasks = count_active_tasks(not_busy_employee)

    for employee in queryset:
        active_tasks = count_active_tasks(employee)
        if active_tasks < min_tasks:
            min_tasks = active_tasks
            not_busy_employee = employee

    active_tasks = count_active_tasks(base_task_executor)
    result = active_tasks - min_tasks
    if result <= 2:
        suitable_employee = base_task_executor
    else:
        suitable_employee = not_busy_employee

    return suitable_employee
