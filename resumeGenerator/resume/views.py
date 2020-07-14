from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'resume/base.html')


@login_required(login_url='login')
def user_details(request):
    return render(request, 'resume/userdetails.html')


