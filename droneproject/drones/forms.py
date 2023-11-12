from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users, AP, Swarms, Drones


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=200, help_text="Required")
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = Users

        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = Users

        fields = [
            "username",
            "email"
        ]


class APForm(forms.ModelForm):

    class Meta:
        model = AP

        fields = [
            "ssid",
            "password",
            "auth_method",
            "updated_by"
        ]
