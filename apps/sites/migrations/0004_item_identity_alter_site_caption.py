# Generated by Django 4.1.2 on 2022-10-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_item_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='identity',
            field=models.CharField(default='item_000', max_length=50, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='site',
            name='caption',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]