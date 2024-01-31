from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): 

    
    """
    We are creating an instance(UserRegisterForm) of an already exiting UserCreationForm in django
    and adding an email field to it.
    
    """
    email = forms.EmailField

    class Meta:
        model = User  #whenever this forms validates, it s going to create a new user, 
        fields = ['username', 'email', 'password1', 'password2']  #fields to be shown on the form