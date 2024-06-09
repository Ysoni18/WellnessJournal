from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class RegisterForm(UserCreationForm):
    
    
    class Meta:
        model = User
        fields = ['username', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={'id':'user', 'size':40,'placeholder':'enter your username'}),
            'password1': forms.PasswordInput(attrs={'id':'password', 'size':'40','placeholder':'enter your password'})
        }
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class teacher_form(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'id':'user'}),
            'password1': forms.PasswordInput(attrs={'id':'password'})
        }
    def __init__(self, *args, **kwargs):
        super(teacher_form, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

