from django import forms
from .models import ExitNote, ExitPass, DayTimeSlot
from django.forms import inlineformset_factory

class ExitNoteForm(forms.ModelForm):
    class Meta:
        model = ExitNote
        fields = ['title', 'description']

class ExitPassForm(forms.ModelForm):
    class Meta:
        model = ExitPass
        fields = '__all__'

class DayTimeForm(forms.ModelForm):
    class Meta:
        model = DayTimeSlot
        fields = ['start_time', 'end_time', 'day_of_week']

DayTimeSlotFormSet = inlineformset_factory(
    ExitPass,  # Родительская модель
    DayTimeSlot,  # Дочерняя модель
    form=DayTimeForm,  # Используемая форма
    extra=5,  # Количество дополнительных форм (по одной на каждый день)
    can_delete=True  # Возможность удаления существующих временных интервалов
)