from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from .forms import PaymentsDetailsRegistrationForm
def payments(request):
    return render(request,"payment.html",{"form":forms})
