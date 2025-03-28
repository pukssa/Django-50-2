from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form


class RegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField()
    password = forms.CharField(max_length = 5)
    avatar = forms.ImageField(required=True)
    age = forms.IntegerField()
    password_confirm = forms.CharField(max_length=5)

def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    password_confirm = cleaned_data.get("password_confirm")
    if (password and password_confirm) and (password != password_confirm):
        raise forms.ValidationError("Passwords don't match")
    return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(max_length = 5, widget=forms.PasswordInput)
