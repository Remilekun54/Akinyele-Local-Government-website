from django.shortcuts import render

# Create your views here.
# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator # Optional: For paginating posts
from django.utils import timezone



def post_list(request):
    """Displays a list of all published blog posts."""
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    
    # Optional Paginator implementation (e.g., 6 posts per page)
    paginator = Paginator(posts, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list, # The list of posts for the current page
    }
    return render(request, 'blog/blog.html', context) # Note the template path

def post_detail(request, slug):
    """Displays the detail of a single blog post using its slug."""
    post = get_object_or_404(Post, slug=slug, publish_date__lte=timezone.now())
    context = {
        'post': post
    }
    return render(request, 'blog/blog-details.html', context) # Note the template path