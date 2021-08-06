from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=100)
    phone=forms.CharField(max_length=11)
    
    class Meta:
        model=User
        fields=['username','email','phone','password1','password2']