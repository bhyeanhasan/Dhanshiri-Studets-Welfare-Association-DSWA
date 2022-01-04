from django import forms
from .models import Student


class Student_form(forms.ModelForm):
    class Meta:
        Faculty = [
            ('cse', 'CSE'),
            ('agri', 'Agriculture'),
            ('bba', 'BBA'),
            ('ansvm', 'ANSVM'),
            ('fisheries', 'Fisheries'),
            ('esdm', 'ESDM'),
            ('lla', 'LLA'),
        ]
        Gender = [
            ('male', 'Male'),
            ('female', 'Female'),
            ('others', 'Others'),
        ]
        Upazila = [
            ('Jhalokathi_sadar', 'Jhalokathi Sadar'),
            ('nalcity', 'Nalcity'),
            ('rajapur', 'Rajapur'),
            ('kathalia', 'Kathalia'),
        ]
        Blood = [
            ('a+', 'A+'),
            ('a-', 'A-'),
            ('b+', 'B+'),
            ('b-', 'B-'),
            ('o+', 'O+'),
            ('o-', 'O-'),
            ('ab+', 'AB+'),
            ('ab-', 'AB-'),
        ]
        model = Student
        fields = ['name', 'faculty', 'session', 'gender', 'upazila', 'address', 'phone', 'blood', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'faculty': forms.Select(choices=Faculty, attrs={'class': 'form-control', }),
            'session': forms.TextInput(attrs={'class': 'form-control', }),
            'gender': forms.Select(choices=Gender,attrs={'class': 'form-control', }),
            'upazila': forms.Select(choices=Upazila,attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            'blood': forms.Select(choices=Blood,attrs={'class': 'form-control', }),
        }
