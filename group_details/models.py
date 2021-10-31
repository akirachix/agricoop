from django.db import models
class Group_details(models.Model):
    date_of_delivery=models.DateField(null=True)
    beans_variety_choice=(
        ('Bush Beans','Bush Beans'),
        ('Climbing Beans','Climbing Beans'),
        ('Ruvuninkingi','Ruvuninkingi')
    )
    beans_variety = models.CharField(
        max_length=800, choices= beans_variety_choice,null=True)
    group_name= models.CharField(
        max_length=120,null=True
    )
    kgs_of_beans= models.PositiveSmallIntegerField(null=True)
    Price_per_kg= models.DateField(null=True)
    total_amount= models.CharField(max_length= 20,null=True)
    total_quantity_purchased= models.PositiveSmallIntegerField(null=True)
# Create your models here.
