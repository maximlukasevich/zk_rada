from django.contrib import admin
from .models import Contacts

class AdminPanel(admin.ModelAdmin):
    list_display = ('contact_type', 'contact')

admin.site.register(Contacts, AdminPanel)
