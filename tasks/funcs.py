def count_active_tasks(employee):
    """Реализует подсчет активных задач сотрудника."""
    active_tasks = 0
    for task in employee.task_set.all():
        if not task.is_completed:
            active_tasks += 1
    return active_tasks
