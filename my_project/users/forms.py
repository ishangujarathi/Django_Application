from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): 

    
    """
    We are creating an instance(UserRegisterForm) of an already exiting UserCreationForm in django
    and adding an email field to it.
    
    """
    email = forms.EmailField()

    class Meta:
        model = User  #whenever this forms validates, it s going to create a new user, 
        fields = ['username', 'email', 'password1', 'password2']  #fields to be shown on the form


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image'] 