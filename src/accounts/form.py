from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =CustomUser
        fields="__all__"
    pass
