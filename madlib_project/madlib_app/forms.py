from django import forms
from .models import MadLibResponse

class MadLibForm(forms.ModelForm):
    class Meta:
        model = MadLibResponse
        fields = '__all__'
