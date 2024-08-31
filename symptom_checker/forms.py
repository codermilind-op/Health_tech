# symptom_checker/forms.py
from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Enter your symptoms (comma-separated)')
