from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib import messages
from .models import ContactMessage # Make sure your ContactMessage model is defined in models.py

# Renders the main contact page (http://127.0.0.1:8000/contact/)
def contact_page(request):
    """
    Renders the contact form template.
    Template: Akinyele/templates/contact.html
    """
    # This assumes your HTML is named 'contact.html' 
    # and is located in your project's main 'templates' folder.
    return render(request, 'contact.html') 

@require_http_methods(["POST"])
def submit_contact_form(request):
    """Handles the POST request when the user submits the form."""
    
    # Get form data using the 'name' attributes from the HTML form
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    # --- Debugging Check ---
    # Check your terminal console immediately after submitting the form.
    # If you see this output, the form submission is reaching the view.
    print(f"--- Form Data Received --- Name: {name}, Subject: {subject}") 

    # Basic Server-side Validation
    if not name or not email or not message:
        # Send an error message back to the template
        messages.error(request, "Please ensure Name, Email, and Message fields are filled.")
        # Redirect back to the contact page
        return redirect(reverse('contact:contact_page')) 

    try:
        # Save the message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Success feedback
        messages.success(request, 'Your message has been successfully sent. Thank you!')
    
    except Exception as e:
        # Log error in console and display user message
        print(f"Error saving contact message to database: {e}") 
        messages.error(request, 'An unexpected error occurred while saving the message. Please try again.')
    
    # Always redirect after a successful POST (Post/Redirect/Get pattern)
    return redirect(reverse('contact:contact_page'))
