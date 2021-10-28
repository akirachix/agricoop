from django import forms
from django.forms import fields
from .models import Bean_details

class BeansDetailsRegistrationForm():
    class Meta:
        model:Bean_details
        fields='__all__'