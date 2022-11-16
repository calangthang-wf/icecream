import email
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import newfeed.urls
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import RegisterForm
from .models import profile

def login_user(request):
    if request.user.is_authenticated:
        return render(request, "pages/already_login.html", {})
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)  #get username, password and check check them against each authentication backend
        
        if user is None:   # If the credentials aren’t valid for any backend or if a backend raises PermissionDenied, it returns None
            context = {"error": "Invalid username or password"}
            return render(request, 'pages/account.html', context)
        login(request, user)
        return HttpResponseRedirect('/')
    return render(request, 'pages/account.html', {})#update data for register_user

def register_user(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            regis = form.save()
            regis.refresh_from_db()   # refresh data
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            user = authenticate(username=username, password=password, email=email)  #get username, password and check check them against each authentication backend
            login(request, user)
            return render(request, "pages/register_ss.html")
        else:
            form = RegisterForm(request.POST)
            return render(request, "pages/regis_err.html")
            
    return render(request, 'pages/resgister.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('/')