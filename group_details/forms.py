from django import forms
from django.forms import fields
from group_details.models import Group_details

class GroupRegistrationForm():
    class Meta:
        model:Group_details
        fields='__all__'