from django.db import models


from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.fields import BigIntegerField, Field



class Payments(models.Model):
    price_per_kg=models.PositiveSmallIntegerField
    total_quantity_purchased=BigIntegerField
    date_of_delivery=models.DateField(auto_now_add=True)
    # group_leader_phonenumberfield=models.phonenumberfield

    


