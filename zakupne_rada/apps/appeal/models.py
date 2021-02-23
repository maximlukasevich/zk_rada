from django.db import models
from django.utils import timezone
import datetime

class Appeals(models.Model):
    appeal_mail = models.CharField('Електронна пошта', max_length = 70, default = '-')
    appeal_message = models.TextField('Текст звернення', default = '-')
    appeal_status = models.BooleanField('Статус виконання', default = False)
    appeal_date = models.DateTimeField('Дата та час відправлення', default = timezone.datetime.now)

    objects = models.Manager()

    def __str__(self):
        return self.appeal_mail

    class Meta:
        verbose_name = 'Звернення'
        verbose_name_plural = 'Звернення'