from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Setting_page
class SettingRegistrationForm(forms.ModelForm):
    class Meta:
        model= Setting_page
        fields= "__all__"