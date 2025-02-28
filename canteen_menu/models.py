from django.db import models


class Allergies(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    allergies = models.ManyToManyField(Allergies, blank=True)
    calories = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=50)
    allergies = models.ManyToManyField(Allergies, blank=True)
    calories = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BreakfastMealSet(models.Model):
    name = models.CharField(max_length=50)
    meals = models.ManyToManyField(Dish, blank=True)
    drinks = models.ManyToManyField(Drink, blank=True)

    def __str__(self):
        return self.name


class LunchMealSet(models.Model):
    name = models.CharField(max_length=50)
    meals = models.ManyToManyField(Dish, blank=True)
    drinks = models.ManyToManyField(Drink, blank=True)

    def __str__(self):
        return self.name


class DinnerMealSet(models.Model):
    name = models.CharField(max_length=50)
    meals = models.ManyToManyField(Dish, blank=True)
    drinks = models.ManyToManyField(Drink, blank=True)

    def __str__(self):
        return self.name


class WeeklyMenus(models.Model):
    starts_on = models.DateField()
    ends_on = models.DateField()
    monday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='monday_breakfast'
    )
    tuesday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='tuesday_breakfast'
    )
    wednesday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='wednesday_breakfast'
    )
    thursday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='thursday_breakfast'
    )
    friday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='friday_breakfast'
    )
    saturday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='saturday_breakfast'
    )
    sunday_breakfast = models.ForeignKey(
        BreakfastMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='sunday_breakfast'
    )
    monday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='monday_lunch'
    )
    tuesday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='tuesday_lunch'
    )
    wednesday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='wednesday_lunch'
    )
    thursday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='thursday_lunch'
    )
    friday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='friday_lunch'
    )
    saturday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='saturday_lunch'
    )
    sunday_lunch = models.ForeignKey(
        LunchMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='sunday_lunch'
    )
    monday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='monday_dinner'
    )
    tuesday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='tuesday_dinner'
    )
    wednesday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='wednesday_dinner'
    )
    thursday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='thursday_dinner'
    )
    friday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='friday_dinner'
    )
    saturday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='saturday_dinner'
    )
    sunday_dinner = models.ForeignKey(
        DinnerMealSet, on_delete=models.CASCADE, blank=True, null=True, related_name='sunday_dinner'
    )
