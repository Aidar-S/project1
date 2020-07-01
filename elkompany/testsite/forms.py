from .models import Tovar
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth import authenticate, login


class TovarForm(ModelForm):
    class Meta:
        model = Tovar
        fields = ["name", "desc", "price"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            }),
            "price": TextInput(attrs={
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
