

from .models import Requests
from django import forms
from django.contrib.auth.models import User, Group


class CreationForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = [
                'title',
                'description',
                'office_number',
                'office_name',
                ]
        
class DenialReasonForm(forms.Form):
    denial_reason = forms.CharField(widget=forms.Textarea, label='Причина отказа', max_length=100)

## Создание поля для выбора пользователя из группы
# class UserInGroupChoiceField(forms.ChoiceField):
#     def __init__(self, group_name, *args, **kwargs):
#         super(UserInGroupChoiceField, self).__init__(*args, **kwargs)
#         group = Group.objects.get(name=group_name)
#         choices = [(user.first_name, user.last_name) for user in User.objects.filter(groups=group)]
#         self.choices = choices
        