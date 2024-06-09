from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class RegisterForm(UserCreationForm):


    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {f:'' for f in fields}


class teacher_form(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {f:'' for f in fields}

