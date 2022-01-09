# Generated by Django 4.0 on 2022-01-01 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_alumni', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=1000)),
                ('designation', models.CharField(default='Member', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('session', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('upazila', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('blood', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]