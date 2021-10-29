from django.shortcuts import render

# Create your views here.
from django import forms
from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm
from .models import Group_list
from django.contrib.auth.decorators import login_required



def home_page(request):
    return render(request,"homepage.html",{"form":forms})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
