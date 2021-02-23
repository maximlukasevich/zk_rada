from django.db import models
from django.utils import timezone
import datetime

class Photos(models.Model):
    photo_title = models.CharField('Підпис фотографії', max_length = 500)
    photo_publication_date = models.DateTimeField('Дата публікації')
    photo = models.ImageField(upload_to='gallery')

    objects = models.Manager()

    def __str__(self):
        return self.photo_title

    class Meta:
        verbose_name = 'Фотографія'
        verbose_name_plural = 'Фотографії'