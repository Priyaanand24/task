# Generated by Django 3.2.4 on 2021-06-11 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller_side', '0003_alter_customers_mobile_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='products',
            new_name='product',
        ),
    ]
