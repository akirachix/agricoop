from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Group_list(models.Model):
    group_name=models.CharField(max_length=100)
    no_of_group_members =models.PositiveSmallIntegerField(null=True)
    group_leader_contact=models.CharField(max_length=20,blank=True, null=True )




class Group_list(models.Model):
    group_name=models.CharField(max_length=100)
    number_of_group_members=models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    name=models.CharField(max_length=100)
    id=models.CharField(max_length=100, primary_key=True)
    phone_number=models.CharField(max_length=100)
   

    def __str__(self):
        return self.user.username
