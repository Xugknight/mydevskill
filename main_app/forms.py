from django import forms
from django.forms import Form, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Skill

class LoginForm(Form):
    username = CharField(label='User Name', max_length=64)
    password = CharField(widget=PasswordInput())

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['description', 'skill_level']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 2, 
                'placeholder': 'Describe your skill'
                }),
                'skill_level': forms.Select(),
        }