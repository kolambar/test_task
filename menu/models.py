from django.db import models

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Вкладка меню')
    previous_tab = models.ForeignKey('self', **NULLABLE, verbose_name='предыдущая вкладка', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
