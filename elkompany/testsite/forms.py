from .models import Tovar
from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ['name', 'desc', 'price']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите цену"
            }),
        }



class LoginForm(forms.Form):
    username = forms.CharField(max_length='50')
    password = forms.CharField(widget=forms.PasswordInput)

    def login_user(self, request):
        user = authenticate(username=self.data['username'],
                            password=self.data['password'])

        if not user is None:
            login(request, user)
        else:
            self.add_error('password', 'Ошибка')


class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
