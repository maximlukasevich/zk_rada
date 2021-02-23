from django.db import models

class Contacts(models.Model):
    contact_type = models.CharField('Тип контанку(email/телефон і тд)', max_length = 500)
    contact = models.TextField('Контактна інформація')

    objects = models.Manager()

    def __str__(self):
        return self.contact

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'
    
