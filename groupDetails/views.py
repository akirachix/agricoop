from django import forms
from django.shortcuts import  render
from .forms import GroupRegistrationForm
from .models import Group_Details

def groupDetails(request):
    return render(request,"groupDetails.html",{"form":forms})

# Create your views here.
