from django.db import models

import datetime
from django.contrib.auth.models import User

# Create your models here.

#*******************************************#
#       ||  Vendor Models Started  ||       #
#*******************************************#

# Add Vendor
class Vendor(models.Model):
    managername = models.CharField(max_length=200)
    vendorname = models.CharField(max_length=200,db_index=True,unique=True)
    joiningdate = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200, db_index=True)
    vendorcontact = models.CharField(max_length=14,db_index=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.vendorname

# Vendor MilkCategory
class MilkCategory(models.Model):
    CHOICES1 = (
        ('Cow','Cow'),
        ('Buffaloe','Buffalo'),#buffaloes
        ('Others','Others'),
    )
    animalname= models.CharField(max_length=200,choices=CHOICES1)
    milkprice = models.FloatField(max_length=200, db_index=True)
    related_vendor = models.ForeignKey(Vendor, related_name='MilkCategory', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.animalname +"----- ₹ " + str(self.milkprice)

# Individual vendor dashboard
class VendorLedger(models.Model):
    related_vendor = models.ForeignKey(Vendor, related_name='vendorledger', on_delete=models.CASCADE,null=True)
    related_milkcategory = models.ForeignKey(MilkCategory, related_name='vendorledger', on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=1000000,db_index=True)
    price = models.FloatField(max_length=1000000,db_index=True,default=0.0)
    quantity = models.FloatField(max_length=1000000,db_index=True,default=0.0)
    total = models.FloatField(max_length=1000000,db_index=True,default=0.0)

    class Meta:
        ordering = ('-date',)
