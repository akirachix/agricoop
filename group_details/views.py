from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from .forms import BeansDetailsRegistrationForm
from .models import Bean_details

def products(request):
    return render(request,"bean_details.html",{"form":forms})

def bean_variety(request):
    product=Bean_details.objects.all()
    return render(request,"bean_details.html",{"product":product})

def group_details(request):
    return render(request,"group_details.html",{"form":forms})