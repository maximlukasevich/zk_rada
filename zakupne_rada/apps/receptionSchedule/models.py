from django.db import models

class ReceptionSSchedules(models.Model):
    position = models.CharField('Посада', max_length = 200)
    fullName = models.CharField('ПІП', max_length = 200)
    dayOfReception = models.CharField('Дні прийому', max_length = 100 )
    receptionHouse = models.CharField('Час прийому', max_length = 100)

    objects = models.Manager()

    def __str__(self):
        return self.fullName
    
    class Meta: 
        verbose_name = 'День прийому'
        verbose_name_plural = 'Дні прийому'
