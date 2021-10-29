from django import forms
from django.forms import fields
from .models import Payments

class PaymentsDetailsRegistrationForm():
    class Meta:
        model:Payments
        fields='__all__'