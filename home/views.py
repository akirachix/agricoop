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

def home_page(request):
    groups = Group_list.objects.all()
    return render(request,"group_list.html",{"groups":groups})
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

