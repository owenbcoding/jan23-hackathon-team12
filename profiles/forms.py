""" Imports for forms and model """
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """ A form to be presenting information based on Profile model """
    class Meta:
        model = Profile
        fields = ('name', 'phone_number', 'email')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
  