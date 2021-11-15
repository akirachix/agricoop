from django.db import models
from django.db.models import fields
from mpesa.models import Login
from mpesa.models import SignUp
from mpesa.models import Payment
from mpesa.models import BaseModel
from mpesa.models import MpesaCalls
from mpesa.models import MpesaCallBacks
from mpesa.models import MpesaPayment
from rest_framework import viewsets
from .serializer import *
class LoginViewSet(viewsets.ModelViewSet):
   queryset=Login.objects.all()
   serializer_class=LoginSerializer
class SignUpViewSet(viewsets.ModelViewSet):
   queryset=SignUp.objects.all()
   serializer_class=SignUpSerializer
class PaymentViewSet(viewsets.ModelViewSet):
   queryset=Payment.objects.all()
   serializer_class=PaymentSerializer
class BaseModelViewset(viewsets.ModelViewSet):
   queryset= BaseModel.objects.all()
   serializer_class=BaseModelSerializer
class MpesaCallsViewset(viewsets.ModelViewSet):
   queryset=MpesaCalls.objects.all()
   serializer_class=MpesaCallsSerializer
class MpesaCallBacksViewset(viewsets.ModelViewSet):
   queryset=MpesaCallBacks.objects.all()
   serializer_class=MpesaCallBacksSerializer
class MpesaPaymentViewset(viewsets.ModelViewSet):
   queryset=MpesaPayment.objects.all()
   serializer_class=MpesaPaymentSerializer
