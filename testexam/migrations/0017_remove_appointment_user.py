# Generated by Django 5.1 on 2024-10-17 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testexam', '0016_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]
