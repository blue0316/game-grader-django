# Generated by Django 4.1.5 on 2023-01-19 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_newgame_eventdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='videolinks',
        ),
    ]