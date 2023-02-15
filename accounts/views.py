from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm, UserLoginForm


def user_register(request):
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
      user.first_name = cd['firstname']
      user.last_name = cd['lastname']
      user.save()
      messages.success(request, 'کاربر با موفقیت ایجاد شد')
      return redirect('home')
  else:
    form = UserRegisterForm()
  return render(request, 'register.html', {'form':form})

def user_login(request):
  if request.method == 'POST':
    form = UserLoginForm(request.POST)
    if form.is_valid():
      temp = form.cleaned_data
      user = authenticate(request, username = temp['username'], password = temp['password'])
      if user is not None:
        login(request, user)
        txt = 'خوش آمدید'+ user.username
        messages.success(request, txt)
        return redirect('user')
      else:
        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')

  else:
    form = UserLoginForm()
  return render(request, 'login.html', {'form':form})

def user(request):
  return render(request, 'user.html')

def user_logout(request):
  logout(request)
  messages.success(request, 'خارج شدید')
  return redirect('home')