# Generated by Django 3.2.8 on 2021-11-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addgroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_list',
            name='group_name',
            field=models.CharField(choices=[('Iwacu group', 'Iwacu group'), ('Komera cooperative', 'Komera cooperative'), ('Ubwiyunge cooperative', 'Ubwiyunge cooperative')], max_length=200, null=True),
        ),
    ]
