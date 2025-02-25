from django.shortcuts import redirect, render
from .models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogForm


@login_required
def get_blogs(request):
    user = request.user
    categories = Category.objects.all()
    get_category = request.GET.get('category')

    if get_category and get_category != "all":
        try:
            category = Category.objects.get(category=get_category) 
            blogs = Blog.objects.filter(category=category, is_draft=False)
        except Category.DoesNotExist:
            blogs = Blog.objects.none()  
    else:
        blogs = Blog.objects.filter(is_draft=False)

    data = {
        "blogs": blogs,
        "categories": categories,
        "selected_category": get_category
    }

    return render(request, "blog/blogs.html", data)


@login_required
def create_blog(request):
    if not request.user.user_type == "1":
        return redirect("blogs")

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  
            blog.save()
            return redirect("doc_blog") 
    else:
        form = BlogForm()

    return render(request, "blog/create_blog.html", {"form": form})


@login_required
def doc_blogs(request):
    user = request.user

    if not user.user_type == "1":
        return redirect("blogs")  
    
    blogs = Blog.objects.filter(author=user.id)

    data = {
        "blogs": blogs,
        "user" : user
    }

    return render(request, "blog/doc_blog.html", data)


