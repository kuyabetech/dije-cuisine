from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from . models import *
# Create your views here.


def home(request):
    companies = Company.objects.all()
    return render(request, 'index.html', {"companies":companies})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        
        if password == password2:
            user = User.objects.create_user(username=email, password=password)
            user.save()
            return redirect('login')
        
        else:
            messages.warning(request, "Password Not Matching!")
            return redirect('register')
        
    return render(request, 'accounts/register.html')

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Email or Password incorrect!')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required
def signout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, "accounts/profile.html")

def company(request):
    companies = Company.objects.all()
    return render(request, 'company.html', locals)