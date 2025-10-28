from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')
        # Map to your HTML form's styling/placeholders
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email*'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Website'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment*', 'rows': 5}),
        }
        labels = {
            'name': '', 
            'email': '', 
            'website': '', 
            'body': '',
        }