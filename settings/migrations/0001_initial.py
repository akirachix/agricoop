# Generated by Django 3.2.4 on 2021-11-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
