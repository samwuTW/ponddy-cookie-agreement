from django.contrib import admin
from .models import AcceptRecord


@admin.register(AcceptRecord)
class AcceptRecordAdmin(admin.ModelAdmin):
    list_display = ('ip', 'user', 'datetime')
    search_fields = ('ip', 'user__email', 'datetime')
