from django.db import models
from django.utils import timezone
import datetime

class News(models.Model):
    news_title = models.CharField('Заголовок новини', max_length = 500)
    news_text = models.TextField('Текст новини')
    news_publication_date = models.DateTimeField('Дата публікації')
    news_image = models.ImageField(upload_to='news_image', null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
    