from django.db import models

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    )

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255, help_text="What matter do you want to see the Chairman about?")
    date_requested = models.DateField(help_text="Preferred date for the appointment")
    message = models.TextField(blank=True, null=True, help_text="Additional details about the appointment")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.get_status_display()})"
