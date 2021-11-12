from django.shortcuts import render
from django import forms
from django.shortcuts import  render, redirect
from group_details.forms import GroupRegistrationForm
from group_details.models import Delivaries
from payments.models import Payments
from addgroup.models import Group_list
from .forms import PaymentsDetailsRegistrationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment


def payments(request):
    return render(request,"payment.html",{"form":forms})


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

def getAccessToken(request):
    consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    consumer_secret = '2nHEyWSD4VjpNh2g'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)
def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 20000,
        "PartyA": 254115626974,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254115626974,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Agricoop",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')
@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://91563395.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://91563395.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)
@csrf_exempt
def call_back(request):
    pass
@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))






