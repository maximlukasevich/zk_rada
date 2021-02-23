from django.contrib import admin
from .models import Documents, Categories, Tags, Sessions

class AdminPanel(admin.ModelAdmin):
    list_display = ('documents_title', 'documents_publication_date', 'document', 'category', 'session')


admin.site.register(Documents, AdminPanel)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Sessions)
