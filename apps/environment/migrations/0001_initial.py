# Generated by Django 4.1.2 on 2022-10-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSetting',
            fields=[
                ('id', models.CharField(default='development', max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Глобальная настройка',
                'verbose_name_plural': 'Глобальные настройки',
            },
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя переменной')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('value', models.CharField(blank=True, max_length=150, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Переменная',
                'verbose_name_plural': 'Переменные',
            },
        ),
    ]
