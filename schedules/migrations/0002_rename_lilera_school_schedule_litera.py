# Generated by Django 5.0.6 on 2024-08-12 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school_schedule',
            old_name='lilera',
            new_name='litera',
        ),
    ]
