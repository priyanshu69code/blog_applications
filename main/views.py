from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    # Retrieve 10 or less recent blog posts
    recent_posts = Blog.objects.order_by('-time_creation')[:10]

    context = {'recent_posts': recent_posts}
    return render(request, "main/home.html", context)


def login_view(request):
    if request.method == 'POST':
        # Retrieve form data
        username_or_email = request.POST['usernameOrEmail']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            # Login the user
            login(request, user)

            # Redirect to a success page (you can change the URL)
            return redirect('home')  # Change 'home' to the desired URL
        else:
            # Authentication failed, show an error message
            context = {'error_message': 'Invalid credentials'}
            return render(request, 'main/login.html', context)

    return render(request, 'main/login.html')


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the passwords match
        if request.POST['password'] != request.POST['confirmPassword']:
            context = {'error_message': 'Passwords do not match'}
            return render(request, 'signup.html', context)

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Authenticate and log in the user
        auth_user = authenticate(request, username=username, password=password)
        login(request, auth_user)

        # Redirect to a success page
        return redirect('home')

    return render(request, 'main/signup.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login/')
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # Save the blog post
            new_blog = form.save(commit=False)
            new_blog.author = request.user  # Set the author to the current logged-in user
            new_blog.save()
            return redirect('home')  # Redirect to the home page or any other desired page after successful creation
    else:
        form = BlogForm()

    return render(request, 'main/create.html', {'form': form})

def view_blog_post(request, blog_id):
    blog_post = get_object_or_404(Blog, blog_id=blog_id)
    return render(request, 'main/readblog.html', {'blog_post': blog_post})

@login_required(login_url='login')
def user_posts(request):
    user_posts = Blog.objects.filter(author=request.user).order_by('-time_creation')
    return render(request, 'main/user_posts.html', {'user_posts': user_posts})

@login_required(login_url='login')
def delete_post(request, blog_id):
    post = get_object_or_404(Blog, blog_id=blog_id)
    
    # Ensure that only the author can delete the post
    if post.author == request.user:
        post.delete()
    
    return redirect('user_posts')

@login_required(login_url='login')
def edit_post(request, blog_id):
    post = get_object_or_404(Blog, blog_id=blog_id)
    
    # Ensure that only the author can edit the post
    if post.author != request.user:
        return redirect('user_posts')
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = BlogForm(instance=post)
    
    return render(request, 'main/edit_post.html', {'form': form, 'post': post})




