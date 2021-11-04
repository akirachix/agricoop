from django.db import models

# Create your models here.
class Setting_page(models.Model):
    account=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30,blank=True, null=True )
