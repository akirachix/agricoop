from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from payments.models import Payments
from .forms import PaymentsDetailsRegistrationForm
def payments(request):
    return render(request,"payment.html",{"form":forms})
def payment_list(request):
    payments=Payments.objects.all()
    return render(request,"payment_list.html",{"payments":payments})





