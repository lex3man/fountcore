# Generated by Django 4.1.2 on 2022-10-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_telegramasset_user_telegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramasset',
            name='state_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Стадия'),
        ),
    ]
