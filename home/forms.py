from django import forms
from.models import Group_list


class GroupRegistrationForm(forms.ModelForm):
    class Meta:
        model = Group_list
        fields='__all__'
        