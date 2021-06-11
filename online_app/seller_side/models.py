import math
import random
from uuid import uuid4

from django.db import models


# function to generate OTP
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# Create your models here.
class Accounts(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    mobile_number = models.CharField(unique=True, max_length=155, null=False)
    otp = models.IntegerField(default=generateOTP)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Store(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    name = models.CharField(max_length=155, null=False)
    address = models.CharField(max_length=155)
    store_link = models.URLField(max_length=255, default='https:www.online_app.com')

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=155, null=False)
    description = models.TextField(null=True)
    mrp = models.IntegerField(null=False)
    sale_price = models.IntegerField(null=False)
    image = models.ImageField(null=True)


class Customers(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=155, null=False, unique=True)
    address = models.CharField(max_length=155)

# class Orders(models.Model):
#     pass
