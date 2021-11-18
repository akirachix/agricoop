from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, response
from django.urls import reverse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0743442637'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        # You can do whatever you want with the notification received from MPESA here.
def stk_timeout(request):
    return HttpResponse(request.body)  

def result_url(request):
    return HttpResponse(request.body)          
