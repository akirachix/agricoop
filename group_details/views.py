from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm
from .models import Group_details

def products(request):
    return render(request,"bean_details.html",{"form":forms})

def bean_variety(request):
    product=Group_details.objects.all()
    return render(request,"bean_details.html",{"product":product})

def group_details(request):
     if request.method=="POST":
        form = GroupRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('group_details')
        else:
            print(form.errors)
     else:
        form= GroupRegistrationForm()
        return render(request,"group_details.html",{"form":form})