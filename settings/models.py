from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Setting_page(models.Model):
    account=models.CharField(max_length=30)
    user_name=models.CharField(max_length=20,null=True)
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    search=models.CharField(max_length=50,null=True)
    message=models.TextField(max_length=5000,null=True)
    phone_number=models.CharField(max_length=30,blank=True, null=True )

