from django import forms
from . import models

class PopularForm(forms.ModelForm):
    class Meta:
        model = models.PopularTeachers
        fields = '__all__'

class ContactsForm(forms.ModelForm):
    class Meta:
        model = models.Contacts
        fields = '__all__'

class StatsForm(forms.ModelForm):
    class Meta:
        model = models.Stats
        fields = '__all__'

class AboutInaiForm(forms.ModelForm):
    class Meta:
        model = models.AboutInai
        fields = '__all__'