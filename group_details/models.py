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
    kgs_of_beans= models.PositiveBigIntegerField(null=True)
    Price_per_kg= models.BigIntegerField(null=True)
    total_amount= models.BigIntegerField(null=True)
# Create your models here.
