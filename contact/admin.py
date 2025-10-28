from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Customizes the view of ContactMessage in the Django Admin."""
    # Columns to display in the list view
    list_display = ('name', 'email', 'subject', 'sent_at')
    # Fields to allow filtering on the right sidebar
    list_filter = ('sent_at',)
    # Fields to allow searching
    search_fields = ('name', 'email', 'subject', 'message')
    # Fields that cannot be changed after creation
    readonly_fields = ('sent_at',)
    # Grouping and ordering of fields in the detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Metadata', {
            'fields': ('sent_at',),
            'classes': ('collapse',), # Optional: collapses the section
        }),
    )
