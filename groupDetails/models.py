from django.db import models

class Group_Details(models.Model):
    group_name=models.CharField(max_length=100)
    number_of_group_members=models.PositiveSmallIntegerField()

# Create your models here.
