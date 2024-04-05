from django import forms

class Addform(forms.Form):
    location=forms.CharField(label='Location',required=False)
    price_per_sqft=forms.FloatField()
