""" Imports for forms and model """
from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    """ A form to test Account model """
    class Meta:
        model = Account
        fields = ('name', 'bank', 'abalance')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'bank': 'Bank',
            'abalance': 'Balance',
        }
  