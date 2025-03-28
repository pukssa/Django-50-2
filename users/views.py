from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from users.models import Profile


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
            avatar = form.cleaned_data['avatar']
            age = form.cleaned_data['age']
            if not User.objects.create_user(email=email, password=password, username=username):
                user = User.objects.create_user(email=email, password=password, username=username)
                if user:
                    Profile.objects.create(user=user, age=age, avatar=avatar)

                elif not user:
                    form.add_error(None,"unknown error")
                    return render(request, 'users/register.html', {'form': form})
            else:
                form.add_error(None,"user with given credentials already exists")
                return render(request, 'users/register.html', {'form': form})

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


def profile_view (request):
    if request.method == 'GET':
        user = request.user
        posts = user.posts.all()
        return render(request, 'users/profile.html', {'user': user, 'posts': posts})




