from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))