# Generated by Django 3.2.5 on 2022-01-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Member', '0002_rename_member_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='designation',
        ),
        migrations.AlterField(
            model_name='student',
            name='blood',
            field=models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('CSE', 'CSE'), ('Agri', 'Agriculture'), ('BBA', 'BBA'), ('Fisheries', 'Fisheries'), ('ESDM', 'ESDM'), ('LLA', 'LLA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='upazila',
            field=models.CharField(choices=[('Jhalokathi_sadar', 'Jhalokathi Sadar'), ('nalcity', 'Nalcity'), ('rajapur', 'Rajapur'), ('kathalia', 'Kathalia')], max_length=100),
        ),
    ]
