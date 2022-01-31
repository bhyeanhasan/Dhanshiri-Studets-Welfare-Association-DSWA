from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=False)
    priority = models.IntegerField(default=1000)
    designation = models.CharField(max_length=100, default="Member")

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=Gender)
    session = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, choices=Faculty)
    upazila = models.CharField(max_length=100, choices=Upazila)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    blood = models.CharField(max_length=20, null=True, blank=True, choices=Blood)
    picture = models.ImageField(upload_to='profile pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ; (approved ={self.is_approved} alumni = {self.is_alumni})'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    priority = models.IntegerField(default=1000)

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(upload_to='profile pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ; (approved ={self.is_approved})'


class Notice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True, blank=True, null=True)
    tittle = models.CharField(max_length=1000)
    body = models.CharField(max_length=10000)
    picture = models.ImageField(blank=True, null=True)
