# Generated by Django 5.0.6 on 2024-09-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_rename_name_lessons_lesson_type_lessons_taught_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_schedule',
            name='group',
            field=models.IntegerField(default=1),
        ),
    ]
