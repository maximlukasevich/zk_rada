from django.contrib import admin
from .models import ReceptionSSchedules

class ReceptionSSchedulesAdm(admin.ModelAdmin):
    list_display = ('position', 'fullName', 'dayOfReception', 'receptionHouse')

admin.site.register(ReceptionSSchedules, ReceptionSSchedulesAdm)
