from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from .forms import UserRegistrationForm, UpdateUserForm, APForm, SwarmsForm, DronesForm
from .models import AP, Swarms, Drones

# Create your views here.
