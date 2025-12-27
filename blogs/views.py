from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Category,Blog,Comment
from django.db.models import Q

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

def blogs(request,slug):
    blog = get_object_or_404(Blog,slug=slug , status = 'Published')
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    #Comments
    comments = Comment.objects.filter(blog=blog)
    comment_count = comments.count()
    context={
        'blog':blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get("keyword")

    try:
        blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status= 'Published')
    except:
        return render(request,'404.html')
    context = {
        'blogs' : blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html',context)