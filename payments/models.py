from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.fields import BigIntegerField

from addgroup.models import Group_list
from group_details.models import Delivaries



class Payments(models.Model):
    total_quantity_purchased=BigIntegerField
    date_of_delivery=models.DateField(auto_now_add=True)
    add_group=models.ForeignKey(Group_list,on_delete=CASCADE ,null=True)
    amount=models.ForeignKey(Delivaries,on_delete=CASCADE,null=True)

class Lipa(models.Model):
    phone_number=models.CharField(max_length=300,null=True)
    pay_bill=models.IntegerField(null=True)
    amount_paid=models.BigIntegerField(null=True)
    