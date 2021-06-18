from datetime import date

from django import forms

from .models import Income, Outcome


class IncomeForm(forms.ModelForm):
    value = forms.DecimalField(initial=100)
    date = forms.DateField(widget=forms.DateInput, initial=date.today())
    type = forms.ChoiceField(choices=Income.ITypes.choices, initial=4)
    repetitive = forms.BooleanField(required=False)
    repetitive_interval = forms.ChoiceField(choices=Income.RInterval.choices, initial=5)
    repetitive_time = forms.IntegerField(initial=0)
    comment = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Income
        fields = [
            "value",
            "date",
            "type",
            "repetitive",
            "repetitive_interval",
            "repetitive_time",
            "comment",
        ]


class OutcomeForm(forms.ModelForm):
    value = forms.DecimalField(initial=100)
    date = forms.DateField(widget=forms.DateInput, initial=date.today())
    type = forms.ChoiceField(choices=Income.ITypes.choices, initial=4)
    repetitive = forms.BooleanField(required=False)
    repetitive_interval = forms.ChoiceField(choices=Income.RInterval.choices, initial=5)
    repetitive_time = forms.IntegerField(initial=0)
    comment = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Outcome
        fields = [
            "value",
            "date",
            "type",
            "repetitive",
            "repetitive_interval",
            "repetitive_time",
            "comment",
        ]
