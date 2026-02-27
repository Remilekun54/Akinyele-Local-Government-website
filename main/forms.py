from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'subject', 'date_requested', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True,
                'style': 'padding: 10px; border: 1px solid var(--accent-color); border-radius: 4px; width: 100%;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True,
                'style': 'padding: 10px; border: 1px solid var(--accent-color); border-radius: 4px; width: 100%;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number',
                'required': True,
                'style': 'padding: 10px; border: 1px solid var(--accent-color); border-radius: 4px; width: 100%;'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject (e.g., Community Development)',
                'required': True,
                'style': 'padding: 10px; border: 1px solid var(--accent-color); border-radius: 4px; width: 100%;'
            }),
            'date_requested': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
                'style': 'padding: 10px; border: 1px solid var(--accent-color); border-radius: 4px; width: 100%;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional Details or Message',
                'style': 'padding: 10px; border: 1px solid var(--accent-color); border-radius: 4px; width: 100%; height: 150px; resize: vertical;'
            }),
        }
