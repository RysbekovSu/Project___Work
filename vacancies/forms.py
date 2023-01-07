from django import forms
from . import models

class VacancyForm(forms.ModelForm):
    class Meta:
        model = models.Vacancy
        fields = '__all__'