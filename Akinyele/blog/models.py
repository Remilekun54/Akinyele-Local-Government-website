
# Create your models here.
# blog/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # For linking to a Django User as the author

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
        ordering = ('-publish_date',) # Order by newest posts first

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        """Returns the URL to access a particular blog post instance."""
        from django.urls import reverse
        # The 'post_detail' URL pattern will be defined in blog/urls.py
        return reverse('post_detail', args=[self.slug])