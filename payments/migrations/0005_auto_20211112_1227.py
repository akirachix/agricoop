# Generated by Django 3.2.8 on 2021-11-12 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_mpesacallbacks_mpesacalls_mpesapayment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaCallBacks',
        ),
        migrations.DeleteModel(
            name='MpesaCalls',
        ),
        migrations.DeleteModel(
            name='MpesaPayment',
        ),
    ]
