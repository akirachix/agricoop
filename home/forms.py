from django import forms
from django.forms import fields
from home.models import Group_list
class GroupRegistrationForm():
    class Meta:
        model:Group_list
        fields='__all__'