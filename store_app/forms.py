from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userProfile
from django import forms


class registration_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class user_profile(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('date_of_birth', 'full_name',)
