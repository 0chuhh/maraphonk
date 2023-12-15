from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class CommonUserCreationForm(UserCreationForm):
    photo = forms.FileField(required=False)
    role = forms.CharField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "middle_name",
            "last_name",
            "image",
            "country",
            "email",
        )

        widgets = {
            "birth_date": DateInput(),
        }


class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
