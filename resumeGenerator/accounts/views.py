from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.


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
                print("Username taken!")
            elif User.objects.filter(email=email).exists():
                print("Email already registered")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password_2)
                user.save()
                print("Yay, you just registered your account with us!")
        else:
            print("Passwords don't match!")
        return HttpResponse("Lets gooo!")
    else:  # This is a GET request, for fetching the registration page.
        return render(request, 'accounts/register.html')
