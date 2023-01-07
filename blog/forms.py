from django import forms
from . import models

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Home
        fields = '__all__'