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


class SwarmsForm(forms.ModelForm):

    class Meta:
        model = Swarms

        fields = [
            "swarm_name",
            "updated_by"
        ]


class DronesForm(forms.ModelForm):
    drone_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Name",
               "style": "width: 125px;"}))

    mac_address = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "XX-XX-XX-XX-XX-XX",
               "style": "width: 140px;"}))

    ip_address = forms.GenericIPAddressField(widget=forms.TextInput(
        attrs={"placeholder": "0.0.0.0",
               "style": "width: 100px;"}))

    class Meta:
        model = Drones

        fields = [
            "drone_name",
            "mac_address",
            "ip_address",
            "swarm_id"
        ]
