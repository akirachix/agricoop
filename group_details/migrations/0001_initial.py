# Generated by Django 3.2.8 on 2021-11-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_delivery', models.DateTimeField(null=True)),
                ('beans_variety', models.CharField(choices=[('Bush Beans', 'Bush Beans'), ('Climbing Beans', 'Climbing Beans'), ('Ruvuninkingi', 'Ruvuninkingi')], max_length=800, null=True)),
                ('group_name', models.CharField(max_length=120, null=True)),
                ('kgs_of_beans', models.PositiveSmallIntegerField(null=True)),
                ('Price_per_kg', models.BigIntegerField(null=True)),
                ('total_amount', models.BigIntegerField(null=True)),
            ],
        ),
    ]
