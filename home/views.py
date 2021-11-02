from django.db import models
from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm

from .models import Group_list




def home_page(request):
    groups = Group_list.objects.all()
    return render(request,"home_page.html",{"group":groups})

def add_group(request):
    if request.method=='POST':
        form=GroupRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GroupRegistrationForm()
    return render(request,"add_group.html",{"form":form})
