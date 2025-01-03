from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import Group
# from django_select2 import Select2MultipleWidget, Select2Widget


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Имя', max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'surname', 'password1', 'password2', 'parents', 'groups']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        self.fields['surname'].label = 'Отчество'
        self.fields['parents'].label = 'Родители'
        self.fields['groups'].label = 'Группы/Роли'
