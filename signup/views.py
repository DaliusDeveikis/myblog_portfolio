from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .forms import UserCreatForm


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signup/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signup:currentsignup')
                # redirect(request.META.get, 'HTTP_REFERER")
            except IntegrityError:
                return render(request, 'signup/signupuser.html', {'form': UserCreationForm(),
                                                                  'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signup/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'signup/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signup/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match!'})
        else:
            login(request, user)
            return redirect('signup:currentsignup')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def createuser_blog(request):
    if request.method == 'GET':
        return render(request, 'signup/createuser.html', {'form': UserCreatForm()})
    else:
        try:
            form = UserCreatForm(request.POST)
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect('signup:currentsignup')
        except ValueError:
            return render(request, 'signup/createuser.html', {'form': UserCreatForm(),'error': 'Bad data passed in. Try again.'})


def currentsignup(request):
    return render(request, 'signup/currentsignup.html')
