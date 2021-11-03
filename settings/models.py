from django.db import models

# Create your models here.
class Setting_page(models.Model):
    account=models.CharField(max_length=30)
    search_button=models.CharField(max_length=50,null=True)
    text_message=models.TextField(max_length=5000,null=True)