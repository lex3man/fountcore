# Generated by Django 4.1.2 on 2022-10-28 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_telegramasset_state_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramasset',
            old_name='state_name',
            new_name='state_id',
        ),
    ]
