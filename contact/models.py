

from django.db import models

class ContactMessage(models.Model):
    """Model to store submissions from the contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    # Automatically records the time the message was received
    sent_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-sent_at'] 
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        # Displays the name and truncated subject in the admin list
        return f"Message from {self.name} ({self.subject[:40]})"
