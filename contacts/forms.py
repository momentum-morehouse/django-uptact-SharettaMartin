from django import forms
from .models import Contact, Note
import datetime


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]
# This sets up the birthdate  field in the form
        widgets = {
        'birthday': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

# This will display the birthdate in output.
#3.1        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["text"]

 