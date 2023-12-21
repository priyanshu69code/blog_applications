from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, "main/home.html")


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


