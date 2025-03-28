from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/register.html', {'form': form})
        elif form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(email=email, password=password, username=username)
            return redirect('/login/')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/login.html', {'form': form})
        elif form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            if not user:
                form.add_error("user with given credentials doesn't exist")
                return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')




