from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('contact',views.contact, name='contact'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('register', views.register, name='register'),
    path('update', views.update, name='update'),

]
