# Generated by Django 4.1.2 on 2022-10-23 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_alter_bot_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150, unique=True, verbose_name='Наименование')),
                ('callback', models.CharField(max_length=50, null=True, verbose_name='Callback')),
                ('row', models.IntegerField(verbose_name='Ряд')),
                ('lang', models.CharField(choices=[('RUS', 'Русский'), ('ENG', 'English')], default='RUS', max_length=10, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Кнопка',
                'verbose_name_plural': 'Кнопки',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150, unique=True, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150, unique=True, verbose_name='Наименование')),
                ('lang', models.CharField(choices=[('RUS', 'Русский'), ('ENG', 'English')], default='RUS', max_length=10, verbose_name='Язык')),
                ('kb_type', models.CharField(max_length=10, verbose_name='Тип клавиатуры')),
                ('buttons', models.ManyToManyField(to='bots.button', verbose_name='Кнопки клавиатуры')),
            ],
            options={
                'verbose_name': 'Клавиатура',
                'verbose_name_plural': 'Клавиатуры',
            },
        ),
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150, unique=True, verbose_name='Наименование')),
                ('lang', models.CharField(choices=[('RUS', 'Русский'), ('ENG', 'English')], default='RUS', max_length=10, verbose_name='Язык')),
                ('content', models.TextField(null=True, verbose_name='Текст')),
                ('delay', models.IntegerField(default=0, verbose_name='Задержка перед ответом (в сек)')),
                ('bot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots.bot', verbose_name='Бот')),
                ('from_button', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots.button', verbose_name='По кнопке')),
                ('keyboard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots.keyboard', verbose_name='Клавиатура')),
                ('next_block', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots.contentblock', verbose_name='Следующий блок')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bots.state', verbose_name='Новый стэйт')),
            ],
            options={
                'verbose_name': 'Блок контента',
                'verbose_name_plural': 'Блоки контента',
            },
        ),
    ]