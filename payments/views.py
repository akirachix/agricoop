from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from group_details.forms import GroupRegistrationForm
from group_details.models import Delivaries
from django.http.response import HttpResponse
from payments.models import Payments
from addgroup.models import Group_list
from .forms import LipaRegistrationForm, PaymentsDetailsRegistrationForm
from django.urls import reverse
from django.http.response import HttpResponseRedirect


def payments(request):
    return render(request,"payment.html",{"forms":forms})


def payment_list(request):
    payments=Payments.objects.all()
    groups=Group_list.objects.all()
    batch=Delivaries.objects.all()
    return render(request,"payment_list.html",{"payments":payments,"groups":groups,"batch":batch})

def edit(request,id):
    groups=Group_list.objects.get(id=id)
    if request.method=="POST":
        form=GroupRegistrationForm(request.POST,instance=groups)
        if form.is_valid():
            form.save() 
            return redirect("payments:payments_list")
    else:
        form=GroupRegistrationForm(instance=groups)
        return render(request,"edit.html",{"form":form})

def delete(request,id):
    payment=Payments.objects.get(id=id)
    if request.method=='POST':
        payment.delete()
        return HttpResponseRedirect(reverse("payments:payments_list"))
    context={"payment":payment}
    return render(request,'delete.html')

def total_amount(self):
    total_amount=self.kgs_of_beans*self.price_per_kg
    return total_amount
    
def lipa(request):
    if request.method=="POST":
        form=LipaRegistrationForm (request.POST)
        if form.is_valid():
            form.save() 
    else:
        form=LipaRegistrationForm()
    return render(request,"payment_list.html",{"form":form})


