from django.contrib import admin
from .models import UploadHistory


@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):

    list_display = (
        'total_equipment',
        'avg_pressure',
        'avg_temperature',
        'uploaded_at'
    )

    ordering = ('-uploaded_at',)

    search_fields = ('total_equipment',)
