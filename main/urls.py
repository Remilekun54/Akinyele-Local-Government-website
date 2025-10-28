


from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # Contact page (handled by the contact app)
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    # Home/Root pages
    path('', views.index_view, name='index'), 
    path('start/', views.start_page_view, name='start_page'),
    path('current/', views.current_view, name='current'),
    
    # Content pages
    path('about/', views.about_view, name='about'),
    path('contact-page/', views.contact_view, name='contact_page'),
    path('services/', views.services_view, name='services'),
    path('service-details/', views.service_details_view, name='service_details'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('team/', views.team_view, name='team'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    
    # Portfolio pages
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio-details/', views.portfolio_details_view, name='portfolio_details'),
    
    
]



