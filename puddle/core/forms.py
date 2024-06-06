from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django import forms


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password1"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "w-full px-4 py-3 rounded-xl"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "w-full px-4 py-3 rounded-xl"
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": "w-full px-4 py-3 rounded-xl"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "w-full px-4 py-3 rounded-xl"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "w-full px-4 py-3 rounded-xl"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm password",
        "class": "w-full px-4 py-3 rounded-xl"
    }))
