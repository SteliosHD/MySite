from django import forms

from django.core.files.base import ContentFile

class ContactForm(forms.Form):
    fname = forms.CharField(label='First Name',max_length=100)
    lname = forms.CharField(label='Last Name',max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Your Message',widget=forms.Textarea)


