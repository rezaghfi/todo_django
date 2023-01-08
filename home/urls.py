from django.urls import path
from . import views
urlpatterns = [
  path('hello/', views.say_hello),
  path('', views.home),
  path('detail/<int:todo_id>/', views.detail)
]