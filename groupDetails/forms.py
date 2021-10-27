from django import forms
from django.forms import fields
from groupDetails.models import Group_Details

class GroupRegistrationForm():
    class Meta:
        model:Group_Details
        fields='__all__'