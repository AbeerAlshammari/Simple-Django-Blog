from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Post, Comment, Category


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def home(request):
    posts = Post.objects.all().order_by('-date_published')
    return render(request, 'main.html', {'posts': posts})


def users_page(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def blogs_page(request):
    posts = Post.objects.all().order_by('-date_published')
    return render(request, 'blogs.html', {'posts': posts})


def comments_page(request):
    comments = Comment.objects.select_related('post', 'user').all()
    return render(request, 'comments.html', {'comments': comments})


def categories_page(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def blog_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogdetails.html', {'post': post})
