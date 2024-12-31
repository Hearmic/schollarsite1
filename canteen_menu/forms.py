from django import forms
from .models import Allergies, BreakfastMealSet, LunchMealSet, DinnerMealSet, Dish, Drink, WeeklyMenus

# Form for Weekly Menus
class MenuForm(forms.ModelForm):
    class Meta:
        model = WeeklyMenus
        fields = '__all__'
        widgets = {
            'starts_on': forms.DateInput(attrs={'type': 'date'}),
            'ends_on': forms.DateInput(attrs={'type': 'date'}),
        }

# --------------------- Creation of Meal Sets ---------------------

# Breakfast Set
class BreakfastSetForm(forms.ModelForm):
    class Meta:
        model = BreakfastMealSet
        fields = ['name']

    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.filter(type="Завтрак"),
        label='Блюда',
        required=True,
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset=Drink.objects.filter(type="Завтрак"),
        label='Напитки',
        required=True,
    )

# Lunch Set
class LunchSetForm(forms.ModelForm):
    class Meta:
        model = LunchMealSet
        fields = ['name']

    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.filter(type="Обед"),
        label='Блюда',
        required=True,
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset=Drink.objects.filter(type="Обед"),
        label='Напитки',
        required=True,
    )

# Dinner Set
class DinnerSetForm(forms.ModelForm):
    class Meta:
        model = DinnerMealSet
        fields = ['name']

    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.filter(type="Полдник"),
        label='Блюда',
        required=True,
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset=Drink.objects.filter(type="Полдник"),
        label='Напитки',
        required=True,
    )

# --------------------- Creation of Dishes ---------------------

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name']

    type = forms.ChoiceField(
        choices=[("Завтрак", "Завтрак"), ("Обед", "Обед"), ("Полдник", "Полдник")],
        required=False,
    )

    possible_allergies = forms.ModelMultipleChoiceField(
        queryset=Allergies.objects.all(),
        label='Возможные аллергии',
        required=False,
    )

# --------------------- Creation of Drinks ---------------------

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['name']

    type = forms.ChoiceField(
        choices=[("Завтрак", "Завтрак"), ("Обед", "Обед"), ("Полдник", "Полдник")],
        required=False,
    )

    possible_allergies = forms.ModelMultipleChoiceField(
        queryset=Allergies.objects.all(),
        label='Возможные аллергии',
        required=False,
    )

# --------------------- Adding Allergies ---------------------

class AddAllergieForm(forms.ModelForm):
    class Meta:
        model = Allergies
        fields = ['name']
