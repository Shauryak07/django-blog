from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    featured_blogs = Blog.objects.all().filter(status= 'Published',is_featured=True).order_by('updated_at')
    blogs = Blog.objects.all().filter(status = 'Published',is_featured = False)

    context = {
        'blogs':blogs,
        'featured_blogs':featured_blogs
    
    }

    return render(request,'home.html',context)