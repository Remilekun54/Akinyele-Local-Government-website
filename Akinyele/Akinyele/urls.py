from django.contrib import admin
from django.urls import path, include
from django.conf import settings # NEW
from django.conf.urls.static import static # NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Contact app handles contact form
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    # Include all URLs from the 'main' app at the root level ('')
    # This makes the index_view accessible directly at http://127.0.0.1:8000/


    # >>> ADD THIS NEW LINE FOR THE BLOG APP <<<
    # This registers the 'blog' namespace
    path('blog/', include('blog.urls', namespace='blog')),

    path('', include('main.urls')),
]

# IMPORTANT: Serve media files only during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)