from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import form, models


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "input_field"}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "input_field"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input_field"}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        
        