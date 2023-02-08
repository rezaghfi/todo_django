from django.urls import path

from accounts import views

urlpatterns  = [
  path('register/', views.user_register, name='register'),
  path('login/', views.user_login, name='login'),
  path('user/', views.user, name='user'),
  path('logout/', views.user_logout, name='logout'),
]