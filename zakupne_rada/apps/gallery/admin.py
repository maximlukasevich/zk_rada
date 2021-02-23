from django.contrib import admin
from .models import Photos

class AdminPanel(admin.ModelAdmin):
    list_display = ('photo_title', 'photo', 'photo_publication_date')
    
admin.site.register(Photos, AdminPanel)
