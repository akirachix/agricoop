from django.db import models
import datetime
from django.db.models.deletion import CASCADE


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
    status_choice=(
        ('Paid','Paid'),
        ('Unpaid','Unpaid'),
        ('Rejected','Rejected')

    )
    status=models.CharField(max_length=90,choices=status_choice,null=True)
    @property
    def total_amount(self):
        total_amount=self.kgs_of_beans* self.price_per_kg
        return total_amount    