from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_home(request):
    posts = BlogPost.objects.filter(status='published').order_by('-created')
    return render(request, 'home.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    return render(request, 'blog_detail.html', {'post': post})

def search_view(request):
    query = request.GET.get('q')
    results = BlogPost.objects.filter(title__icontains=query, status='published') if query else []
    return render(request, 'search_results.html', {'query': query, 'results': results})
