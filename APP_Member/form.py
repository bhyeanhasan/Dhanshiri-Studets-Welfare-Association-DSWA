from django import forms
from .models import Student, Teacher, Notice, NoticeImages


class Student_form(forms.ModelForm):
    class Meta:
        Faculty = [
            ('CSE', 'CSE'),
            ('Agri', 'Agriculture'),
            ('BBA', 'BBA'),
            ('Fisheries', 'Fisheries'),
            ('ESDM', 'ESDM'),
            ('LLA', 'LLA'),
        ]
        Gender = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),
        ]
        Upazila = [
            ('Jhalokathi Sadar', 'Jhalokathi Sadar'),
            ('Nalcity', 'Nalcity'),
            ('Rajapur', 'Rajapur'),
            ('Kathalia', 'Kathalia'),
        ]
        Blood = [
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
        ]
        model = Student
        fields = ['name', 'faculty', 'session', 'gender', 'upazila', 'address', 'phone', 'blood', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'faculty': forms.Select(choices=Faculty, attrs={'class': 'form-control', }),
            'session': forms.TextInput(attrs={'class': 'form-control', }),
            'gender': forms.Select(choices=Gender, attrs={'class': 'form-control', }),
            'upazila': forms.Select(choices=Upazila, attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            'blood': forms.Select(choices=Blood, attrs={'class': 'form-control', }),
        }


class Teacher_form(forms.ModelForm):
    class Meta:
        Faculty = [
            ('CSE', 'CSE'),
            ('Agri', 'Agriculture'),
            ('BBA', 'BBA'),
            ('Fisheries', 'Fisheries'),
            ('ESDM', 'ESDM'),
            ('LLA', 'LLA'),
        ]
        Designation = [
            ('Professor', 'Professor'),
            ('Associate Professor', 'Associate Professor'),
            ('Assistant Professor', 'Assistant Professor'),
            ('Lecturer', 'Lecturer'),
        ]
        Upazila = [
            ('Jhalokathi Sadar', 'Jhalokathi Sadar'),
            ('Nalcity', 'Nalcity'),
            ('Rajapur', 'Rajapur'),
            ('Kathalia', 'Kathalia'),
        ]

        model = Teacher
        fields = ['name', 'designation', 'faculty', 'department', 'upazila', 'address', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'faculty': forms.Select(choices=Faculty, attrs={'class': 'form-control', }),
            'designation': forms.Select(choices=Designation, attrs={'class': 'form-control', }),
            'upazila': forms.Select(choices=Upazila, attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            'department': forms.TextInput(attrs={'class': 'form-control', }),
        }



