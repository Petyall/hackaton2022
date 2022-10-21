from operator import truediv
from django.db import IntegrityError
from urllib import request
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import os
from pathlib import Path
import mimetypes
from authentification.forms import UserRegistrationForm, UserLoginForm
from django.http.response import HttpResponse

from authentification.models import Schedule


def registration_student(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'user_form': user_form})

def registration_teacher(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'user_form': user_form})

def registration_worker(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'user_form': user_form})

def register(request):
    return render(request, 'auth/select.html')


def login_user(request):
    context = {'login_form': UserLoginForm()}
    if request.method == "POST":
        # Эта строка берёт всё, что написал пользователь
        # И помещает в переменную login_form для дальнейшего действия
        login_form = UserLoginForm(request.POST)
        # Если введенные данные пройдут валидацию, то выполнится условие
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # Это условие проверки пароля (подошел или нет)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь {username} или пароль не были найдены!'
                }
        # Если пользователь не зарегистрирован или пароль не подошёл,
        # то будет выполнятся это условие, которое будет брать ответ из forms.py
        # А в последствии выводится в login.html через цикл
        else:
            context = {
                'login_form': login_form,
            }
    return render(request, 'auth/login.html', context)



def logout_user(request):
    logout(request)
    return redirect('index')



def profile(request):
    return render(request, 'auth/profile.html')

def download_file(request):

    group = request.user.first_name
    # Define Django project base directory
    BASE_DIR = Path(__file__).resolve().parent.parent
    base_str = str(BASE_DIR)
    # Define text file name

    # for g in Schedule.get_groups(request):
    #     if User.first_name == g:
    #         filegroup = Schedule.group+'.xlsx'
    #     else:
    #         pass
    # a = User.first_name

    filename = group+'.xlsx'
    # Define the full file path
    filepath = base_str + "\\schedule\\" + filename
    print(filepath)
    
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
