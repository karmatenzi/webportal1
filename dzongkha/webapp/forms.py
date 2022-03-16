from dataclasses import fields
from pyexpat import model
from django import forms
from .models import ContactDetails

class ContactDetailsForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields= ('firstname', 'lastname', 'email', 'comments')