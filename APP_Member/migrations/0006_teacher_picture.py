# Generated by Django 3.2.5 on 2022-01-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Member', '0005_auto_20220131_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile pictures'),
        ),
    ]
