# from GreenKiosk.mpesa.models import BaseModel, MpesaCallBacks, MpesaCalls,MpesaPayment
from mpesa.models import *
from mpesa.models import Login
from mpesa.models import SignUp
from mpesa.models import Payment
from rest_framework import serializers
class LoginSerializer(serializers.ModelSerializer):
   class Meta:
       model=Login
       fields=("email","password")
class SignUpSerializer(serializers.ModelSerializer):
   class Meta:
       model=SignUp
       fields=("first_name","last_name","email","password","confirm_password")
class PaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model=Payment
       fields=("phone_number","amount")
class MpesaCallsSerializer(serializers.ModelSerializer):
   class Meta:
       model=MpesaCalls
       fields=("  ip_address","caller","conversation_id","content")
class MpesaCallBacksSerializer(serializers.ModelSerializer):
   class Meta:
       model=MpesaCallBacks
       fields=("  ip_address","caller","conversation_id","content")
class MpesaPaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model=MpesaPayment
       fields=("amount","first_name","middle_name","last_name","phone_number","organization_balance")
class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
       model=BaseModel
       fields=("updated_at","created_at")