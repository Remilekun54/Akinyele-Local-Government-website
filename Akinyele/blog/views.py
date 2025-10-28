# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect # Added 'redirect'
from .models import Post, Comment # Added 'Comment'
from .forms import CommentForm # NEW: Import the CommentForm
from django.core.paginator import Paginator
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

# ----------------------------------------------------------------------
# UPDATED post_detail FUNCTION
def post_detail(request, slug):
    """
    Displays the detail of a single blog post and handles comment submission.
    """
    post = get_object_or_404(Post, slug=slug, publish_date__lte=timezone.now())
    
    # 1. Retrieve existing, approved comments for this post
    comments = post.comments.filter(active=True)
    
    # 2. Handle comment form submission (POST request)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment (active=False by default for moderation)
            new_comment.save()
            
            # Use redirect to prevent form resubmission on page refresh
            # Assuming your URL name is 'post_detail' in blog/urls.py
            return redirect('blog:post_detail', slug=post.slug) 
            
    # 3. Handle initial page load (GET request) or invalid form
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,           # Pass comments to the template
        'comment_form': comment_form,   # Pass form to the template
    }
    return render(request, 'blog/blog-details.html', context)
# ----------------------------------------------------------------------