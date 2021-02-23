from django.contrib import admin
from .models import News

class AdminPanel(admin.ModelAdmin):
    list_display = ('news_title', 'news_publication_date')

admin.site.register(News, AdminPanel)
