from django.db import models
from django.utils import timezone
import datetime

class Vacancies(models.Model):
    vacancy_name = models.CharField('Назва вакансії', max_length = 700)
    vacancy_number = models.IntegerField('Кількість вакансій', null = True, blank = True)
    vacancy_criterion = models.TextField('Критерії', null = True, blank = True)
    vacancy_salary = models.CharField('Зарплата', null = True, blank = True, max_length = 50)
    vacancy_contact = models.CharField('Контактна інформація для звернення', max_length = 500)
    vacancy_publication_date = models.DateTimeField('Дата публікації')

    objects = models.Manager()

    def __str__(self):
        return self.vacancy_name

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'
    
