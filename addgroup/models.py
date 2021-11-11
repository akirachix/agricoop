from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Group_list(models.Model):
    group_name_choice= (
        ('Iwacu group','Iwacu group'),
        ('Komera cooperative','Komera cooperative'),
        ('Ubwiyunge cooperative','Ubwiyunge cooperative'),
        )
    group_name=models.CharField(max_length=200,choices= group_name_choice,null=True)
    no_of_members=models.PositiveSmallIntegerField()
    profile = models.ImageField(default='default.jpg', upload_to='static/images', null=True)
    id=models.CharField(max_length=100, primary_key=True)
    phone_number=models.CharField(max_length=100)
   
    