from django import forms
from .models import ContactMessage, SubscribeEmail


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]


class SubsribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeEmail
        fields = ["email"]
