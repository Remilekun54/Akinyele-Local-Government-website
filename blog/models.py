# blog/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """Model representing a single blog post."""
    
    # Core Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="A short label for the URL, containing only letters, numbers, underscores or hyphens.")
    content = models.TextField()
    
    # Metadata
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.CharField(max_length=50, default='Uncategorized')
    
    # Date/Time
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # Image Upload
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post_detail', args=[self.slug]) # Adjusted to use 'blog' namespace
        
# ----------------------------------------------------------------------
# NEW COMMENT MODEL
class Comment(models.Model):
    """Model representing a single comment on a blog post."""
    # Links the comment back to the Post model
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    # Fields from your HTML form
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True) # Optional website field
    body = models.TextField()
    
    # Metadata
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False) # For comment moderation

    class Meta:
        ordering = ['created_on'] # Oldest comment first

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'