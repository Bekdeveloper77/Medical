# Generated by Django 5.1 on 2024-09-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testexam', '0005_question_alter_medecine_options_answer_useranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
