# contact/urls.py

from django.urls import path
from . import views

# Change the namespace to something unique, like 'contact_app'
app_name = 'contact_app' 

urlpatterns = [
    # URL for viewing the contact form (e.g., mysite.com/contact/)
    path('', views.contact_page, name='contact_page'), 
    
    # URL for processing the form submission (e.g., mysite.com/contact/submit/)
    path('submit/', views.submit_contact_form, name='submit_form'), 
]