from django import forms
from django.shortcuts import  render
from .forms import GroupRegistrationForm
from .models import Group_details

def group_details(request):
    return render(request,"group_details.html",{"form":forms})

# Create your views here.
