from django.db import models
import datetime
from django.db.models.deletion import CASCADE

from addgroup.models import Group_list



class Delivaries(models.Model):
    group_name=models.ForeignKey(Group_list,max_length=200,null=True,on_delete=CASCADE)
    date_of_delivery=models.DateTimeField(null=True)
    beans_variety_choice= (
        ('Bush beans','Bush beans'),
        ('Climbing beans','Climbing beans'),
        ('Ruvuninkingi','Ruvuninkingi'),
        )
    beans_variety=models.CharField(max_length=200,choices= beans_variety_choice,null=True)
    kgs_of_beans= models.PositiveSmallIntegerField(null=True)
    price_per_kg=models.PositiveSmallIntegerField(null=True)

    @property
    def total_amount(self):
        total_amount=self.kgs_of_beans* self.price_per_kg
        return total_amount    

    def __str__(self):
        return self.group_name.group_name    


