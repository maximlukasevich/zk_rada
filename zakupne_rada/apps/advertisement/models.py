from django.db import models
from django.utils import timezone
import datetime

class Advertisements(models.Model):
    ad_title = models.CharField('Заголовок оголошення', max_length = 500)
    ad_text = models.TextField('Текст оголошення')
    ad_publication_date = models.DateTimeField('Дата публікації')
    ad_image = models.ImageField(upload_to='ad_image', null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.ad_title

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'
    
