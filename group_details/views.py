from django import forms
from django.shortcuts import redirect, render
from .forms import GroupRegistrationForm
from django.shortcuts import render
from .models import Group_details
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
