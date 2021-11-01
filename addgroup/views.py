from django.contrib.auth.models import Group
from django.shortcuts import render

from django import forms
from django.shortcuts import  render, redirect

from addgroup.models import Group_list
from .forms import GroupRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def add_group(request):
    if request.method=="POST":
        form=GroupRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=GroupRegistrationForm()
    return render(request,"add_group.html",{"form":form})

def display_group(request):
    groups= Group_list.objects.all()
    return render(request,"display_group.html", {"groups":groups})
