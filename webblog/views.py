from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-pub_date')[:2]
    otherblogsdata = Blog.objects.order_by('-pub_date')[2:]
    return render(request, 'webblog/home.html', {'blogs' : blogs, 'otherblogs': otherblogsdata})


def blog_page(request, pk):
    blogdata = Blog.objects.get(id = pk)
    otherblogsdata = Blog.objects.exclude(id = pk)
    return render(request, 'webblog/blog-page.html', {'blog': blogdata, 'otherblogs': otherblogsdata})
