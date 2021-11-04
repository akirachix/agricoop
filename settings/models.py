from django.db import models

# Create your models here.
class Setting_page(models.Model):
    account=models.CharField(max_length=30)

class privacy_info(models.Model):
    phone_number=models.CharField(max_length=30,blank=True, null=True )
