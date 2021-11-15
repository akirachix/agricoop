from django.db import models
# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField( max_length=12, null=True)
    last_name = models.CharField(max_length=15, null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=15, null=True)
    confirm_password=models.CharField(max_length=15, null=True)
class Login(models.Model):
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=15, null=True)
class Payment(models.Model):
    phone_number=models.CharField(max_length=15, null=True)
    amount=models.IntegerField()



