from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Group_list(models.Model):
    group_name=models.CharField(max_length=100)
    no_of_members=models.PositiveSmallIntegerField()
    profile = models.ImageField(default='default.jpg', upload_to='profile_images', null=True)
    id=models.CharField(max_length=100, primary_key=True)
    phone_number=models.CharField(max_length=100)
   
    