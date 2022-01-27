from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .form import Student_form
from .models import Student


def index(request):
    return render(request, 'main.html')


def contact(request):
    return render(request, 'contact.html')


def members(request):
    students = Student.objects.filter(is_approved=True).order_by('session', 'priority')
    return render(request, 'members.html', {'students': students})


def alumni(request):
    students = Student.objects.filter(is_alumni=True).order_by('session')
    return render(request, 'members.html', {'students': students})


def committee(request):
    students = Student.objects.filter(is_alumni=False).order_by('priority')
    return render(request, 'members.html', {'students': students})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        messages.info(request, 'Invalid Username/Password')

    return render(request, "member/login.html", {})


def logout_user(request):
    logout(request)
    return redirect("index")


@login_required(login_url='login')
def profile(request):
    if Student.objects.filter(user=request.user).exists():
        user_profile = Student.objects.get(user=request.user)
        return render(request, 'member/profile.html', {'user_profile': user_profile})
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
            address = form.cleaned_data['address']

            Student.objects.create(user=user, name=name, faculty=faculty, session=session, gender=gender,
                                   upazila=upazila, phone=phone, blood=blood, address=address)

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
        if pass1 == pass2:
            User.objects.create_user(username, email, pass1)
            return redirect('register')
        messages.info(request, 'Information Updated')


    return render(request, 'member/user signup.html')



def update(request):
    student = Student.objects.get(user=request.user)
    form = Student_form(request.POST or None, instance=student)
    if form.is_valid():
        user = request.user
        name = form.cleaned_data['name']
        faculty = form.cleaned_data['faculty']
        session = form.cleaned_data['session']
        gender = form.cleaned_data['gender']
        upazila = form.cleaned_data['upazila']
        address = form.cleaned_data['address']
        phone = form.cleaned_data['phone']
        blood = form.cleaned_data['blood']

        student.name = name
        student.faculty = faculty
        student.session = session
        student.gender = gender
        student.upazila = upazila
        student.address = address
        student.phone = phone
        student.blood = blood

        student.save()
        messages.info(request, 'Information Updated')

    return render(request, 'member/update.html', {'form': form, 'student': student})


def update_image(request):
    student = Student.objects.get(user=request.user)
    if 'picture' in request.FILES:
        student.picture.delete()
        student.picture = request.FILES['picture']
        student.save()
        messages.info(request, 'Profile Picture Changed')
        return redirect('update')

    messages.info(request, 'Please select a photo')
    return redirect('update')


def update_pass(request):
    olspass = request.POST['oldpass']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    if pass1 != pass2 or pass1 == '':
        messages.info(request, 'Password not matched')
        return redirect('update')
    if pass1 == '':
        messages.info(request, 'Please input a valid password')
        return redirect('update')

    if request.user.check_password(olspass):
        request.user.set_password(pass2)
        request.user.save()
        update_session_auth_hash(request, request.user)
        messages.info(request, 'Password Changed')
        return redirect('update')

    else:
        messages.info(request, 'Wrong Password')
        return redirect('update')


def update_email(request):
    email = request.POST['email']
    student = request.user
    student.email = email
    student.save()
    messages.info(request, 'Email Changed')
    return redirect('update')
