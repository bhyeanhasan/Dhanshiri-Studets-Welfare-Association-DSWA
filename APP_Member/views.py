from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import Student_form
from .models import Student


def index(request):
    return render(request, 'main.html')


def contact(request):
    return render(request, 'contact.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "member/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("index")


@login_required(login_url='login')
def profile(request):
    try:
        user_profile = Student.objects.get(user=request.user)
        return render(request, 'member/profile.html', {'user_profile': user_profile})
    except:
        return redirect('register')


@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            faculty = form.cleaned_data['faculty']
            session = form.cleaned_data['session']
            gender = form.cleaned_data['gender']
            upazila = form.cleaned_data['upazila']
            phone = form.cleaned_data['phone']
            blood = form.cleaned_data['blood']

            Student.objects.create(user=user, name=name, faculty=faculty, session=session, gender=gender,
                                   upazila=upazila, phone=phone, blood=blood)

            return redirect('profile')
    else:
        form = Student_form()

    return render(request, 'member/register.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        print(username + email + pass1 + pass2)
        if pass1 == pass2:
            User.objects.create_user(username, email, pass1)
            return redirect('register')

        return render(request, 'member/user signup.html')
    else:
        return render(request, 'member/user signup.html')


def update(request):
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        name = request.POST['name']
        faculty = request.POST['faculty']
        session = request.POST['session']
        gender = request.POST['gender']
        upazila = request.POST['upazila']
        phone = request.POST['phone']
        blood = request.POST['blood']
        student.name = name
        student.faculty = faculty
        student.session = session
        student.gender = gender
        student.upazila = upazila
        student.phone = phone
        student.blood = blood
        student.save()
        return redirect('profile')
    return render(request,'member/update profile.html')
