from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields
from .models import Delivaries

class GroupRegistrationForm(forms.ModelForm):
    class Meta:
        model= Delivaries
        fields= "__all__"

# class BeanRegistrationForm(forms.ModelForm):
#     class Meta:
#         model=Bean_details
#         fields="__all__"     