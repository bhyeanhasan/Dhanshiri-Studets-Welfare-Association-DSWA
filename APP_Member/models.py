from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=False)
    priority = models.IntegerField(default=1000)
    designation = models.CharField(max_length=100,default="Member")
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    session = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    blood = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ; (approved ={self.is_approved} alumni = {self.is_alumni})'
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=False)
    priority = models.IntegerField(default=1000)
    designation = models.CharField(max_length=100,default="Member")
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    session = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    blood = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ; (approved ={self.is_approved} alumni = {self.is_alumni})'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    priority = models.IntegerField(default=1000)
    designation = models.CharField(max_length=100,default="Member")
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ; (approved ={self.is_approved} '
