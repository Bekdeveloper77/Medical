# Generated by Django 5.1 on 2024-11-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testexam', '0018_remove_appointment_type_of_disease_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('message_text', models.TextField()),
                ('response_text', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]