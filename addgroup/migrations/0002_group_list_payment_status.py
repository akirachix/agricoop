# Generated by Django 3.2.9 on 2021-11-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addgroup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_list',
            name='payment_status',
            field=models.CharField(default='Unpaid', max_length=240, null=True),
        ),
    ]
