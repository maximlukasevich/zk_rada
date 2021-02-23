from django.db import models

class Group(models.Model):
    name = models.CharField('Партія', max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партія'
        verbose_name_plural = 'Партії'

class Deputies(models.Model):
    fullName = models.CharField('ПІП', max_length = 150)
    group = models.ForeignKey(Group, blank = True, null = True,  on_delete = models.SET_NULL)
    workPlace = models.CharField('Місце роботи', max_length = 200)
    position = models.CharField('Посада', max_length = 75)
    pollingStation = models.TextField('Виборча дільниця')
    photo = models.ImageField(upload_to = 'deputies', null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
            return self.fullName

    class Meta:
        verbose_name = 'Депутат'
        verbose_name_plural = 'Депутати'
    
