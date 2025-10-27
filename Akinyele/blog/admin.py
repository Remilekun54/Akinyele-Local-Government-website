
# Register your models here.
# blog/admin.py

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Customizes how the Post model is displayed in the admin interface."""
    list_display = ('title', 'author', 'publish_date', 'category', 'updated_date')
    list_filter = ('publish_date', 'author', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Auto-fill slug field based on title
    raw_id_fields = ('author',) # Use a search widget for author selection
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)