from django import forms
from .models import Fuel

class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = ['name', 'description', 'price', 'photo_url']
