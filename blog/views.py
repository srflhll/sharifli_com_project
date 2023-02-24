from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator


def all_blogs(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 10)  # Set the number of items per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    # commented by hsh blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
