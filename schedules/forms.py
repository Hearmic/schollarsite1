from django import forms
from .models import *

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = '__all__'

    lesson_type = forms.ChoiceField(
        choices=[
            ('Математика', 'Математика'),
            ('Геометрия','Геометрия'),
            ('Алгебра','Алгебра'),
            ('Русский язык', 'Русский язык'),
            ('Русская литература', 'Русская литература'),
            ('Английский язык', 'Английский язык'),
            ('Инфоррматика','Инфоррматика'),
            ('История Казахтана', 'История Казахтана'),
            ('История мира', 'История мира'),
            ('География', 'География'),
            ('Физика', 'Физика'),
            ('Химия', 'Химия'),
            ('Биология', 'Биология'),
            ('Музыка', 'Музыка'),
            ('Художественный труд', 'Художественный труд'),
            ('Физкультура', 'Физкультура'),
            ('Психология', 'Психология'),
            ('Познание мира', 'Познание мира'),
        ],
    )


class SchoolScheduleForm(forms.ModelForm):
    class Meta:
        model = school_schedule
        fields = '__all__'
        