# Generated by Django 5.0.6 on 2024-09-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('found_in', models.IntegerField()),
                ('found_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
