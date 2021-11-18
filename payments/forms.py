from django import forms
from django.forms import fields
from .models import Lipa, Payments

class PaymentsDetailsRegistrationForm():

    class Meta:
        model:Payments
        fields='__all__'


class LipaRegistrationForm():   
    class Meta:
        model:Lipa
        fields='__all__'