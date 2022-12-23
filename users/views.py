import random
from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from users.forms import RegisterForm


def signup(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, 'users/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('users:login')


def login(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                from django.contrib.auth import login
                login(request, user)
                return redirect('/home_tests/home')
    context = {
        'form': AuthenticationForm(),
    }
    return render(request, 'users/login.html', context=context)
