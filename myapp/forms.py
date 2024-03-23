from django import forms
from .models import NewProperty

class PropertyForm(forms.ModelForm):
    class Meta:
        model=NewProperty
        fields='__all__'
