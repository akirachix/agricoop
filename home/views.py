from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from .forms import BeansDetailsRegistrationForm
from .models import Bean_details

def products(request):
    return render(request,"products.html",{"form":forms})

def bean_variety(request):
    product=Bean_details.objects.all()
    return render(request,"products.html",{"product":product})    