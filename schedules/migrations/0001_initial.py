# Generated by Django 5.0.6 on 2024-08-12 07:38

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
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_on', models.DateField()),
                ('ends_on', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='club_lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('club', models.CharField(max_length=20)),
                ('classrom', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('lesson', models.IntegerField()),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('classroom', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='school_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('lilera', models.CharField(max_length=1)),
                ('friday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson1', to='schedules.lessons')),
                ('friday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson2', to='schedules.lessons')),
                ('friday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson3', to='schedules.lessons')),
                ('friday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson4', to='schedules.lessons')),
                ('friday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson5', to='schedules.lessons')),
                ('friday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson6', to='schedules.lessons')),
                ('friday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson7', to='schedules.lessons')),
                ('friday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson8', to='schedules.lessons')),
                ('friday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lesson9', to='schedules.lessons')),
                ('monday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson1', to='schedules.lessons')),
                ('monday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson2', to='schedules.lessons')),
                ('monday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson3', to='schedules.lessons')),
                ('monday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson4', to='schedules.lessons')),
                ('monday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson5', to='schedules.lessons')),
                ('monday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson6', to='schedules.lessons')),
                ('monday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson7', to='schedules.lessons')),
                ('monday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson8', to='schedules.lessons')),
                ('monday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lesson9', to='schedules.lessons')),
                ('saturday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson1', to='schedules.lessons')),
                ('saturday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson2', to='schedules.lessons')),
                ('saturday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson3', to='schedules.lessons')),
                ('saturday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson4', to='schedules.lessons')),
                ('saturday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson5', to='schedules.lessons')),
                ('saturday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson6', to='schedules.lessons')),
                ('saturday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson7', to='schedules.lessons')),
                ('saturday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson8', to='schedules.lessons')),
                ('saturday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lesson9', to='schedules.lessons')),
                ('sunday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson1', to='schedules.lessons')),
                ('sunday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson2', to='schedules.lessons')),
                ('sunday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson3', to='schedules.lessons')),
                ('sunday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson4', to='schedules.lessons')),
                ('sunday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson5', to='schedules.lessons')),
                ('sunday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson6', to='schedules.lessons')),
                ('sunday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson7', to='schedules.lessons')),
                ('sunday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson8', to='schedules.lessons')),
                ('sunday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lesson9', to='schedules.lessons')),
                ('thursday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson1', to='schedules.lessons')),
                ('thursday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson2', to='schedules.lessons')),
                ('thursday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson3', to='schedules.lessons')),
                ('thursday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson4', to='schedules.lessons')),
                ('thursday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson5', to='schedules.lessons')),
                ('thursday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson6', to='schedules.lessons')),
                ('thursday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson7', to='schedules.lessons')),
                ('thursday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson8', to='schedules.lessons')),
                ('thursday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lesson9', to='schedules.lessons')),
                ('tuesday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson1', to='schedules.lessons')),
                ('tuesday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson2', to='schedules.lessons')),
                ('tuesday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson3', to='schedules.lessons')),
                ('tuesday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson4', to='schedules.lessons')),
                ('tuesday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson5', to='schedules.lessons')),
                ('tuesday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson6', to='schedules.lessons')),
                ('tuesday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson7', to='schedules.lessons')),
                ('tuesday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson8', to='schedules.lessons')),
                ('tuesday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lesson9', to='schedules.lessons')),
                ('wednesday_lesson1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson1', to='schedules.lessons')),
                ('wednesday_lesson2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson2', to='schedules.lessons')),
                ('wednesday_lesson3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson3', to='schedules.lessons')),
                ('wednesday_lesson4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson4', to='schedules.lessons')),
                ('wednesday_lesson5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson5', to='schedules.lessons')),
                ('wednesday_lesson6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson6', to='schedules.lessons')),
                ('wednesday_lesson7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson7', to='schedules.lessons')),
                ('wednesday_lesson8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson8', to='schedules.lessons')),
                ('wednesday_lesson9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lesson9', to='schedules.lessons')),
            ],
        ),
    ]
