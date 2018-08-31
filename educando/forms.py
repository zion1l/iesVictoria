from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Contraseña'}))

class CreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
