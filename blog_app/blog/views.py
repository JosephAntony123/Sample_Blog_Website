from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout



def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

def post_details(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'details.html', {'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('home')

@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'edit_post.html', {'form': form, 'post': post})
    else:
        return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
