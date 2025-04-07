from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def user_login(request):
    return render(request, 'user_auth/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return redirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return redirect(reverse('user_auth:show_user'))

def show_user(request):
    return render(request, 'user_auth/user.html', {
        "username": request.user.username,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_auth:login'))
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})