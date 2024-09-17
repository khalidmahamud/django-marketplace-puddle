from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Username",
                "class": "w-full py-4 px-6 rounded-md",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Email Address",
                "class": "w-full py-4 px-6 rounded-md",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your Password",
                "class": "w-full py-4 px-6 rounded-md",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Your Password",
                "class": "w-full py-4 px-6 rounded-md",
            }
        )
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Username",
                "class": "w-full py-4 px-6 rounded-md",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your Password",
                "class": "w-full py-4 px-6 rounded-md",
            }
        )
    )
