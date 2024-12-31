from django import forms
from .models import allergies, breakfast_MealSet, lunch_MealSet, dinner_MealSet, dish, drink, WeeklyMenus


class MenuForm(forms.ModelForm):
    class Meta:
        model = WeeklyMenus
        fields = '__all__'
        widgets = {
            'starts_on': forms.DateInput(attrs={'type': 'date'}),
            'ends_on': forms.DateInput(attrs={'type': 'date'}),
        }
################################################  Создание наборов блюд #############################################

#---Завтрак---#
class BreakfastSetForm(forms.ModelForm):
    class Meta:
        model = breakfast_MealSet
        fields = ['name']
    dishes = forms.ModelMultipleChoiceField(
        queryset= dish.objects.filter(type="Завтрак"),
        label = 'Блюда',
        required= True
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset= drink.objects.filter(type="Завтрак"),
        label = 'Напитки',
        required= True
    )    
#---Обед---#
class LunchSetForm(forms.ModelForm):
    class Meta:
        model = lunch_MealSet
        fields = ['name']
    dishes = forms.ModelMultipleChoiceField(
        queryset= dish.objects.filter(type="Обед"),
        label = 'Блюда',
        required= True
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset= drink.objects.filter(type="Обед"),
        label = 'Напитки',
        required= True
    )  
#---Полдник---#
class DinnerSetForm(forms.ModelForm):
    class Meta:
        model = dinner_MealSet
        fields = ['name']
    dishes = forms.ModelMultipleChoiceField(
        queryset=dish.objects.filter(type="Полдник"),
        label = 'Блюда',
        required= True
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset= drink.objects.filter(type="Полдник"),
        label = 'Напитки',
        required= True
    )

################################################  Создание блюд  ###################################################

class DishForm(forms.ModelForm):
    class Meta:
        model = dish
        fields =['name']

    type =forms.ChoiceField(
        choices=["Завтрак", "Обед", "Полдник"],
        required=False
        )

    possible_allergies = forms.ModelMultipleChoiceField(
        queryset= allergies.objects.all(),
        label = 'Возможные аллергии',
        required= False
    )    

################################################  Создание напитков #################################################

class DrinkForm(forms.ModelForm):
    class Meta:
        model = drink
        fields =['name']
        
    type =forms.ChoiceField(
        choices=["Завтрак", "Обед", "Полдник"],
        required=False
        )
    
    possible_allergies = forms.ModelMultipleChoiceField(
        queryset= allergies.objects.all(),
        label = 'Возможные аллергии',
        required= False
    )    


######################################################  Добавление аллергий #########################################################

class AddAllergieForm(forms.ModelForm):
    class Meta:
        model = allergies
        fields = ['name']