# Generated by Django 5.1 on 2024-08-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testexam', '0003_about_aboutachive_aboutin_appointment_doctorself_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Sarlavhasi')),
                ('info', models.CharField(max_length=500, verbose_name='Malumoti')),
            ],
            options={
                'verbose_name': 'Patients',
                'verbose_name_plural': 'Patients',
            },
        ),
    ]
