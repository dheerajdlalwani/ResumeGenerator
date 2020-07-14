from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':  # When the user fills the form, and submits it, the data comes as a POST request, because we have set the method as "POST" for security purpose.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password_1 = request.POST['password_first']
        password_2 = request.POST['password_second']
        email = request.POST['email']

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username not available!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password_2)
                user.save()
                messages.info(request, 'Yay, you just registered your account with us!')
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match!")
            return redirect('signup')
    else:  # This is a GET request, for fetching the registration page.
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
