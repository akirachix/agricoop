from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Group_details

class GroupRegistrationForm(forms.ModelForm):
    class Meta:
        model= Group_details
        fields= "__all__"