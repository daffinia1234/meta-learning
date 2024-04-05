from django import forms
from myapp.models import NewProperty, Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PropertyForm(forms.ModelForm):
    class Meta:
        model=NewProperty
        fields='__all__'

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        fields='__all__'

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

