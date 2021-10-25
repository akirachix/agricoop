
from django import forms
from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm
from .models import Group_list
def home_page(request):
    return render(request,"homepage.html",{"form":forms})