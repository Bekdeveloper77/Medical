# Generated by Django 5.1 on 2024-11-26 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testexam', '0025_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]