from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.template.defaultfilters import slugify

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context={
        'category_count' : category_count,
        'blog_count' : blog_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/add_category.html',context)

def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context= {
        'form' : form,
        'category' : category,
    }
    return render(request, 'dashboard/edit_category.html',context)


def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


def blogs(request):
    blogs = Blog.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request,'dashboard/blogs.html',context)

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            blog.slug = slugify(form.cleaned_data['title']) + '-' + str(blog.id)
            blog.save()
            return redirect('blogs')
    form = BlogForm()
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/add_blog.html',context)


def edit_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = slugify(form.cleaned_data['title']) + '-' + str(blog.id)
            blog.save()
            return redirect('blogs')
    form = BlogForm(instance=blog)
    context= {
        'form' : form,
        'blog' : blog,
    }
    return render(request, 'dashboard/edit_blog.html',context)

def delete_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    blog.delete()
    return redirect('blogs')
