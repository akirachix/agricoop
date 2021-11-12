from django.db import models
import datetime
from django.db.models.deletion import CASCADE

from addgroup.models import Group_list


class Delivaries(models.Model):

    group_name_choice= (
        ('Iwacu group','Iwacu group'),
        ('Komera cooperative','Komera cooperative'),
        ('Ubwiyunge cooperative','Ubwiyunge cooperative'),
        )
    group_name=models.CharField(max_length=200,choices= group_name_choice,null=True)
    date_of_delivery=models.DateTimeField(null=True)
    beans_variety_choice= (
        ('Bush beans','Bush beans'),
        ('Climbing beans','Climbing beans'),
        ('Ruvuninkingi','Ruvuninkingi'),
        )
    beans_variety=models.CharField(max_length=200,choices= beans_variety_choice,null=True)
    kgs_of_beans= models.PositiveSmallIntegerField(null=True)
    price_per_kg=models.PositiveSmallIntegerField(null=True)
    # group=models.ForeignKey(Group_list ,on_delete=CASCADE,null=True)
   
   

    @property
    def total_amount(self):
        total_amount=self.kgs_of_beans* self.price_per_kg
        return total_amount    


# class Bean_details(models.Model):

#     # beans_variety_choice= (
#     #     ('Bush beans','Bush beans'),
#     #     ('Ruvuninkingi','Ruvuninkingi'),
#     #     ('Climbing beans','Climbing beans'),
#     #     )
#     beans_variety = models.CharField(max_length=30,null=True)
#     price_per_kg=models.PositiveSmallIntegerField(null=True)

    
# def create_varieties():
#     new = Bean_details.objects.bulk_create([
#     Bean_details(beans_variety = 'Bush Beans' ),
#     Bean_details(beans_variety = 'Ruvuninkingi' ),
#     Bean_details(beans_variety = 'Climbing Beans' ),
  
#         ])
#     return new  