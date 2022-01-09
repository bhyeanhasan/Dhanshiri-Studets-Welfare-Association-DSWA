from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import Student_form
from .models import Student


def index(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "registration/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("index")


@login_required(login_url='login')
def profile(request):

    profile_check = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('index')
    else:
        form = Student_form()

    return render(request, 'form.html', {'form': form})
