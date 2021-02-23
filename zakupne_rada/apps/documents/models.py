import os
import uuid
from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

class Categories(models.Model):

    category_name = models.CharField('Назва категорії', max_length = 500)
    
    objects = models.Manager()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Tags(models.Model):
    tag = models.CharField(max_length=100)  

    objects = models.Manager()

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Sessions(models.Model):
    number = models.CharField('Номер сесії', max_length = 30)

    objects = models.Manager()

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = 'Сесія'
        verbose_name_plural = 'Сесії'

class Documents(models.Model):
    documents_title = models.CharField('Назва документу', max_length = 500)
    documents_text = models.TextField('Опис документу')
    documents_publication_date = models.DateTimeField('Дата публікації')
    document = models.FileField('Документ', upload_to='documents')
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tags, blank = True)
    session = models.ForeignKey(Sessions, blank = True, null = True,  on_delete = models.SET_NULL)
    
    objects = models.Manager()

    def __str__(self):
        return self.documents_title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документи'

@receiver(models.signals.post_delete, sender=Documents)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.document:
        if os.path.isfile(instance.document.path):
            os.remove(instance.document.path)
