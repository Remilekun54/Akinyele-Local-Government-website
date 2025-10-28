# blog/urls.py

from django.urls import path
from . import views

# >>> ADD THIS LINE: Define the application namespace <<<
app_name = 'blog'

urlpatterns = [
    # Blog List Page (e.g., /blog/)
    path('', views.post_list, name='post_list'),
    
    # Blog Detail Page (e.g., /blog/my-first-post-slug/)
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]