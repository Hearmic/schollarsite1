# Generated by Django 5.0.6 on 2024-07-26 11:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='exit_note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deactivate_on', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_denied', models.BooleanField(default=False)),
                ('qr_code', models.ImageField(upload_to='')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_note_created_by', to=settings.AUTH_USER_MODEL)),
                ('denied_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_note_denied_by', to=settings.AUTH_USER_MODEL)),
                ('parent_approved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_note_parent_approved', to=settings.AUTH_USER_MODEL)),
                ('security_approved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_note_security_approved', to=settings.AUTH_USER_MODEL)),
                ('teacher_approved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exit_note_teacher_approved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]