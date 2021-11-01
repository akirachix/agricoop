from django import forms
from django.forms import fields
from addgroup.models import Group_list
from.models import Group_list

class GroupRegistrationForm(forms.ModelForm):
    class Meta:
        model = Group_list
        fields='__all__' 

