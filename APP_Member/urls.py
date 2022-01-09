from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
]
