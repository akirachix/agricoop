# Generated by Django 3.2.8 on 2021-11-17 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0006_auto_20211117_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivaries',
            name='payment_status',
        ),
    ]
