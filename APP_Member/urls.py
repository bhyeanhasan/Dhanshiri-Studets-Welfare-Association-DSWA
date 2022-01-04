from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('student', views.student_register, name="student_register"),
    path('login', auth_views.LoginView.as_view(), name='login'),
]
