from django.db import models
from django.utils import timezone
import datetime

class Cards(models.Model):
    card_title = models.CharField('Заголовок карточки', max_length = 500)
    card_text = models.TextField('Текст карточки')
    card_publication_date = models.DateTimeField('Дата публікації')
    card_image = models.ImageField(upload_to='card_image', null = True, blank = True)
    
    objects = models.Manager()

    def __str__(self):
        return self.card_title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
