# Generated by Django 5.0.6 on 2025-01-19 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exit_notes', '0003_alter_exit_note_created_by_alter_exit_note_denied_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exit_note',
            name='deactivate_on',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 19, 15, 36, 2, 698440, tzinfo=datetime.timezone.utc)),
        ),
    ]
