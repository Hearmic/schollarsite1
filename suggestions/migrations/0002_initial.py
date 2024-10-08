# Generated by Django 5.0.6 on 2024-07-24 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suggestions', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='voters_against',
            field=models.ManyToManyField(blank=True, related_name='against_suggestions', to='users.user'),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='voters_for',
            field=models.ManyToManyField(blank=True, related_name='for_suggestions', to='users.user'),
        ),
    ]
