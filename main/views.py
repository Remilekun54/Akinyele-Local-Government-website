# main/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment request has been submitted successfully! We will get back to you soon.')
            return redirect('book_appointment')
        else:
            messages.error(request, 'There was an error in your submission. Please check the form and try again.')
    else:
        form = AppointmentForm()
    
    return render(request, 'book_appointment.html', {'form': form})

# Home page views
def index_view(request):
    """Loads the index.html template (homepage)"""
    return render(request, 'index.html')

def start_page_view(request):
    """Loads the start-page.html template"""
    return render(request, 'start-page.html')

def current_view(request):
    """Loads the current.html template"""
    return render(request, 'current.html')


# Content pages
def about_view(request):
    """Loads the about.html template"""
    return render(request, 'about.html')

def contact_view(request):
    """Loads the contact.html template"""
    # NOTE: The 'contact' app is for handling form submission, 
    # but this is for displaying the template under the 'main' app structure.
    return render(request, 'contact.html')

def services_view(request):
    """Loads the services.html template"""
    return render(request, 'services.html')

def service_details_view(request):
    """Loads the service-details.html template"""
    return render(request, 'service-details.html')

def pricing_view(request):
    """Loads the pricing.html template"""
    return render(request, 'pricing.html')

def team_view(request):
    """Loads the team.html template"""
    return render(request, 'team.html')

def testimonials_view(request):
    """Loads the testimonials.html template"""
    return render(request, 'testimonials.html')


# Portfolio pages
def portfolio_view(request):
    """Loads the portfolio.html template"""
    return render(request, 'portfolio.html')

def portfolio_details_view(request):
    """Loads the portfolip-details.html template"""
    return render(request, 'portfolio-details.html')


# Blog pages
def blog_view(request):
    """Loads the blog.html template"""
    return render(request, 'blog.html')

def blog_details_view(request):
    """Loads the blog-details.html template"""
    return render(request, 'blog-details.html')

