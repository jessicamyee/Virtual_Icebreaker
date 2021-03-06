from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Registration(UserCreationForm):
    team_name = forms.CharField(max_length=30, required=True)


    class Meta:
        model = User
        fields = ('username', 'team_name', 'password1', 'password2', )