from django.shortcuts import render
from blogs.models import Category,Blog
from assignment.models import About

def home(request):
    featured_blogs = Blog.objects.all().filter(status= 'Published',is_featured=True).order_by('updated_at')
    blogs = Blog.objects.all().filter(status = 'Published',is_featured = False)
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'blogs':blogs,
        'featured_blogs':featured_blogs,
        'about' : about,

    }

    return render(request,'home.html',context)