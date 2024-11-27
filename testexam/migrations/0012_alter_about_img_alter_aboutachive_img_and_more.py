# Generated by Django 5.1 on 2024-09-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testexam', '0011_alter_doctorself_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/images/about', verbose_name='Img'),
        ),
        migrations.AlterField(
            model_name='aboutachive',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/images/about', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='aboutin',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/images/about', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='medecine',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/images/medicine', verbose_name='Img'),
        ),
        migrations.AlterField(
            model_name='onepage',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/images/onepage', verbose_name='Img'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/images/partner', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/images/service', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/images/specialist', verbose_name='Img'),
        ),
    ]
