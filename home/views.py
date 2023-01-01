from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Todo


def say_hello(request):
  # return HttpResponse("hello")
  person = {'name':'reza', 'age':29}
  return render(request, 'hello.html', context=person)

def home(request):
  all = Todo.objects.all()
  return render(request, 'home.html', {'todos': all})