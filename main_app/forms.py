from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Skill, Note

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a username',
            'class': 'input-field',
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'input-field',
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
            'class': 'input-field',
        })
    )

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
                'placeholder': 'Describe your skill',
                'class': 'input-field',
                }),
                'skill_level': forms.Select(attrs={'class': 'input-field'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Add a note',
                'class': 'input-field',
            })
        }