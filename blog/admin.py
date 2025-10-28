
# Register your models here.
# blog/admin.py

from django.contrib import admin
from .models import Post, Comment

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



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        # Action to quickly approve comments
        queryset.update(active=True)
    approve_comments.short_description = "Approve selected comments"