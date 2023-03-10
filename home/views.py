from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import TodoCreateForm, TodoUpdateForm
from .models import Todo


def say_hello(request):
  # return HttpResponse("hello")
  reza = {'name': 'reza', 'age': 29, 'range': range(9)}
  admin = {'name': 'admin', 'age': 28, 'range': range(10)}
  user = {'name': 'user', 'age': 3}
  return render(request, 'hello.html', context=admin)


def home(request):
  todos = Todo.objects.all()
  return render(request, 'home.html', {'todos': todos})


def detail(request, todo_id):
  todo = Todo.objects.get(id=todo_id)
  return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  messages.success(request, 'کار با موفقیت حذف شد')
  return redirect('home')


def create(request):
  if request.method == 'POST':
    form = TodoCreateForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
      messages.success(request, 'کار جدید با موفقیت ایجاد شذ')
      return redirect('home')
  else:
    form = TodoCreateForm()
  return render(request, 'create.html', {'form': form})


def update(request, todo_id):
  todo = Todo.objects.get(id=todo_id)
  if request.method == 'POST':
    form = TodoUpdateForm(request.POST, instance=todo)
    if form.is_valid():
      form.save()
      messages.success(request, 'کار بروزرسانی شد')
      return redirect('detail', todo_id)
  else:
    form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
