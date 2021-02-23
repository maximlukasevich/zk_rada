from django.contrib import admin
from .models import Deputies, Group

class AdminPanel(admin.ModelAdmin):
    list_display = ('fullName', 'group', 'workPlace', 'position', 'pollingStation', 'photo')

admin.site.register(Deputies, AdminPanel)
admin.site.register(Group)
