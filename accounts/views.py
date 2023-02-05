from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm


def user_register(request):
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
      messages.success(request, 'کاربر با موفقیت ایجاد شد')
      return redirect('home')
  else:
    form = UserRegisterForm()
  return render(request, 'register.html', {'form':form})
