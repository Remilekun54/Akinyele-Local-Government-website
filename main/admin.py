from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date_requested', 'status', 'created_at')
    list_filter = ('status', 'date_requested')
    search_fields = ('name', 'email', 'subject')
