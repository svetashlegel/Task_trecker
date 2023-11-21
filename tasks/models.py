from django.db import models
from employees.models import Employee


NULLABLE = {'blank': True, 'null': True}


class Task(models.Model):

    title = models.CharField(max_length=200, verbose_name='наименование задачи')
    base_task = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='основополагающая задача')
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, **NULLABLE, verbose_name='исполнитель')
    deadline = models.DateField(**NULLABLE, verbose_name='срок сдачи')
    is_completed = models.BooleanField(default=False, verbose_name='задача завершена')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

