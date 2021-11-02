from django import forms
from django.shortcuts import  render, redirect
from .forms import PaymentsDetailsRegistrationForm
from .models import Payments
from payments.models import Payments


def payments(request):
    return render(request,"payment.html",{"form":forms})

def payment_list(request):
    payments=Payments.objects.all()
    return render(request,"payment_list.html",{"payments":payments})
