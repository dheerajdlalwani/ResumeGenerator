from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to Resume Generator! We will help you generate a professional resume, so that you "
                        "get that dream job!")

def user_details(request):

    return render(request, 'resume/userdetails.html')



