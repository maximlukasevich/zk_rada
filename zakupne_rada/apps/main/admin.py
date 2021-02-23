from django.contrib import admin
from .models import Cards

class AdminPanel(admin.ModelAdmin):
    list_display = ('card_title', 'card_text', 'card_publication_date')

admin.site.register(Cards, AdminPanel)
