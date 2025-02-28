# Generated by Django 5.0.6 on 2025-01-20 07:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_moderated', models.BooleanField(default=False)),
                ('is_denied', models.BooleanField(default=False)),
                ('votes_for', models.IntegerField(default=0)),
                ('max_votes_for', models.IntegerField(default=500)),
                ('votes_against', models.IntegerField(default=0)),
                ('max_votes_against', models.IntegerField(default=300)),
                ('denial_reason', models.CharField(blank=True, max_length=100, verbose_name='Причина отказа')),
                ('restricted_to_groups', models.ManyToManyField(blank=True, to='auth.group')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voters_against', models.ManyToManyField(blank=True, related_name='against_suggestions', to=settings.AUTH_USER_MODEL)),
                ('voters_for', models.ManyToManyField(blank=True, related_name='for_suggestions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
