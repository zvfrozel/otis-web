# Generated by Django 3.1.8 on 2021-04-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210403_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='zoom_room_url',
            new_name='classroom_url',
        ),
    ]
