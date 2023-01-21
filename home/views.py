from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Todo


def say_hello(request):
  # return HttpResponse("hello")
  reza = {'name':'reza', 'age':29, 'range':range(9)}
  admin = {'name':'admin', 'age':28, 'range':range(10)}
  user = {'name':'user', 'age': 3}
  return render(request, 'hello.html', context=admin)

def home(request):
  all = Todo.objects.all()
  return render(request, 'home.html', {'todos': all})

def detail(request, todo_id):
  todo = Todo.objects.get(id= todo_id)
  return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  messages.success(request, 'کار با موفقیت حذف شد')
  return redirect('home')