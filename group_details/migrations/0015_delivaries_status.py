# Generated by Django 3.2.8 on 2021-11-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0014_delivaries_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivaries',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Rejected', 'Rejected')], max_length=90, null=True),
        ),
    ]
