# Generated by Django 3.2.8 on 2021-11-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0004_auto_20211101_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_details',
            name='total_amount',
            field=models.BigIntegerField(max_length=20, null=True),
        ),
    ]
