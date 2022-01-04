from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import Student_form


def index(request):
    return render(request, 'index.html')



def student_register(request):
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = Student_form()

    return render(request, 'form.html', {'form': form})
