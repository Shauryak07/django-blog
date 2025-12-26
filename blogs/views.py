from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Category,Blog

# Create your views here.
def blogs_by_category(request,category_id):
    category_blogs = Blog.objects.filter(status='Published',category=category_id)
    
    category = get_object_or_404(Category,id=category_id)
    
    # try : 
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')
    context = {
        'blogs' : category_blogs, 
        'category' : category,
    }

    return render(request, 'blogs_by_category.html', context)