from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('registration/', include('django.contrib.auth.urls')),
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('profile/<username>/', views.profile_view, name="profile_view"),
    path('contact',views.contact, name='contact'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('register', views.register, name='register'),
    path('update', views.update, name='update'),
    path('update_image', views.update_image, name='update_image'),
    path('update_pass', views.update_pass, name='update_pass'),
    path('update_email', views.update_email, name='update_email'),
    path('members', views.members, name='members'),
    path('teacher', views.teacher, name='teacher'),
    path('alumni', views.alumni, name='alumni'),
    path('committee', views.committee, name='committee'),
    path('sendMail', views.sendMail, name='sendMail'),
    path('notice', views.notice, name='notice'),
    path('view/<id>/', views.view, name='view'),
    path('delete_notice/<id>/', views.delete_notice, name='delete_notice'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)