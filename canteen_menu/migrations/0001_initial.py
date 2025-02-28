# Generated by Django 5.0.6 on 2025-01-19 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('type', models.CharField(max_length=20)),
                ('allergies', models.ManyToManyField(blank=True, to='canteen_menu.allergies')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('type', models.CharField(max_length=20)),
                ('allergies', models.ManyToManyField(blank=True, to='canteen_menu.allergies')),
            ],
        ),
        migrations.CreateModel(
            name='DinnerMealSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('meals', models.ManyToManyField(blank=True, to='canteen_menu.dish')),
                ('drinks', models.ManyToManyField(blank=True, to='canteen_menu.drink')),
            ],
        ),
        migrations.CreateModel(
            name='BreakfastMealSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('meals', models.ManyToManyField(blank=True, to='canteen_menu.dish')),
                ('drinks', models.ManyToManyField(blank=True, to='canteen_menu.drink')),
            ],
        ),
        migrations.CreateModel(
            name='LunchMealSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('drinks', models.ManyToManyField(blank=True, to='canteen_menu.drink')),
                ('meals', models.ManyToManyField(blank=True, to='canteen_menu.dish')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyMenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_on', models.DateField()),
                ('ends_on', models.DateField()),
                ('friday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_breakfast', to='canteen_menu.breakfastmealset')),
                ('friday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_dinner', to='canteen_menu.dinnermealset')),
                ('friday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_lunch', to='canteen_menu.lunchmealset')),
                ('monday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_breakfast', to='canteen_menu.breakfastmealset')),
                ('monday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_dinner', to='canteen_menu.dinnermealset')),
                ('monday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_lunch', to='canteen_menu.lunchmealset')),
                ('saturday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_breakfast', to='canteen_menu.breakfastmealset')),
                ('saturday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_dinner', to='canteen_menu.dinnermealset')),
                ('saturday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_lunch', to='canteen_menu.lunchmealset')),
                ('sunday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_breakfast', to='canteen_menu.breakfastmealset')),
                ('sunday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_dinner', to='canteen_menu.dinnermealset')),
                ('sunday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_lunch', to='canteen_menu.lunchmealset')),
                ('thursday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_breakfast', to='canteen_menu.breakfastmealset')),
                ('thursday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_dinner', to='canteen_menu.dinnermealset')),
                ('thursday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_lunch', to='canteen_menu.lunchmealset')),
                ('tuesday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_breakfast', to='canteen_menu.breakfastmealset')),
                ('tuesday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_dinner', to='canteen_menu.dinnermealset')),
                ('tuesday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_lunch', to='canteen_menu.lunchmealset')),
                ('wednesday_breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_breakfast', to='canteen_menu.breakfastmealset')),
                ('wednesday_dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_dinner', to='canteen_menu.dinnermealset')),
                ('wednesday_lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_lunch', to='canteen_menu.lunchmealset')),
            ],
        ),
    ]
