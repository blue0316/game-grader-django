# Generated by Django 4.1.5 on 2023-01-11 09:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False),
        ),
    ]
