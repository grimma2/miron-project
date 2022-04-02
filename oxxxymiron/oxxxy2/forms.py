from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'photo', 'slug', 'pub_date']


class UserRegister(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserAuthentication(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')
