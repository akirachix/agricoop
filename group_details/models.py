from django.db import models

class Group_details(models.Model):
    group_name=models.CharField(max_length=100)
    number_of_group_members=models.PositiveSmallIntegerField()
    bean_type=models.CharField
    Quantity=models.BigIntegerField
    price=models.BigIntegerField
    date_of_Delivary=models.DateField
    status= models.BooleanField
    group_leader=models.CharField
    batch_number=models.OneToOneField
# Create your models here.
