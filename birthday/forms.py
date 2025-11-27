from django import forms
from .models import Birthdays


class BirthdaysForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Birthdays
        fields = ["name", "birth_date"]
