import datetime
from django import forms
from trap.models import Traps


class CreateNewTrap(forms.ModelForm):
    creation_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.datetime.now())
    name = forms.TextInput()
    # An inline class to provide additional information on the form.

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Traps
        fields = '__all__'
