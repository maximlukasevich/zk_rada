from django.contrib import admin
from .models import Appeals

class AppealsAmd(admin.ModelAdmin):
    list_display = ('appeal_mail', 'appeal_message', 'appeal_status', 'appeal_date')
    list_filter = ('appeal_status', 'appeal_date')

admin.site.register(Appeals, AppealsAmd)
