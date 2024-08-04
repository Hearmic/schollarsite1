from django import forms
from .models import allergies, breakfast_MealSet, lunch_MealSet, dinner_MealSet, dish, drink

class MenuForm(forms.Form):
    starts_on = forms.DateField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=True)
    #############################  Понедельни  ####################################
    monday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    monday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    monday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
    #############################  Вторник  ####################################
    tuesday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    tuesday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    tuesday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
    #############################  Среда  ####################################
    wednesday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    wednesday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    wednesday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
    #############################  Четверг  #################################### 
    thursday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    thursday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    thursday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
    #############################  Пятница  ####################################
    friday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    friday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    friday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
    #############################  Суббота  ####################################
    saturday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    saturday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    saturday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
    #############################  Воскресенье  ####################################
    sunday_breakfast = forms.ModelChoiceField(
        queryset=breakfast_MealSet.objects.all(),
        label='На завтрак:',
        required=True
    )
    sunday_lunch = forms.ModelChoiceField(
        queryset=lunch_MealSet.objects.all(),
        label='На обед:',
        required=True
    )
    sunday_dinner = forms.ModelChoiceField(
        queryset=dinner_MealSet.objects.all(),
        label='На полдник:',
        required=True
    )
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