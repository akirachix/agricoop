from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BigIntegerField


class Bean_details(models.Model):
    # bean_variety=models.OneToOneField(Group_Details,on_delete=models.CASCADE,primary_key=True)
    price_per_kg=models.PositiveSmallIntegerField
    total_quantity_purchased=BigIntegerField
    date_of_delivery=models.DateField(auto_now_add=True)
    

