# Generated by Django 3.2.4 on 2021-06-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_side', '0002_alter_store_store_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='mobile_number',
            field=models.CharField(max_length=155, unique=True),
        ),
    ]
