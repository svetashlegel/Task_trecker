from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Employee(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='имя')
    second_name = models.CharField(max_length=100, verbose_name='фамилия')
    position = models.CharField(max_length=50, verbose_name='должность')

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.position}'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

