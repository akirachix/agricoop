from django.db import models
# Create your models here.
class Setting_page(models.Model):
    account=models.CharField(max_length=30)
    search=models.CharField(max_length=50,null=True)
    message=models.TextField(max_length=5000,null=True)
