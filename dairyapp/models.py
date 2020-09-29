import datetime
from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    managername = models.CharField(max_length=200)
    vendorname = models.CharField(max_length=200,db_index=True,unique=True)
    joiningdate = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200, db_index=True)
    vendorcontact = models.CharField(max_length=14,db_index=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.vendorname

#Vendor MilkCategory
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


class vendorledger(models.Model):
    related_vendor = models.ForeignKey(Vendor, related_name='vendorledger', on_delete=models.CASCADE,null=True)
    related_milkcategory = models.ForeignKey(MilkCategory, related_name='vendorledger', on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=1000000,db_index=True)
    price = models.FloatField(max_length=1000000,db_index=True,default=0.0)
    quantity = models.FloatField(max_length=1000000,db_index=True,default=0.0)
    total = models.FloatField(max_length=1000000,db_index=True,default=0.0)

    class Meta:
        ordering = ('-date',)

#**************************************************************************************************************
#Customer Models (User)
#**************************************************************************************************************

class Profile(models.Model):
    CHOICES1 = (
        ('Admin','Admin'),
        ('Customer','Customer'),
        ('Manager','Manager'),
        )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, null=True, blank=False,choices=CHOICES1)
    contact_number = models.CharField(max_length=20,null=True,unique=True)
    joining_data = models.DateField(auto_now_add=False)
    address = models.CharField(max_length=500,null=True)


    class Meta:
        ordering = ('-user_type',)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class CustomerMilkCategory(models.Model):
    CHOICES1 = (
        ('Cow','Cow'),
        ('Buffaloe','Buffalo'),#buffaloes
        ('Others','Others'),
    )
    animalname= models.CharField(max_length=200,choices=CHOICES1)
    milkprice = models.FloatField(max_length=200, db_index=True)
    related_customer = models.ForeignKey(User, related_name='CustomerMilkCategory', on_delete=models.CASCADE, null=True)



    def fullname(self):
        return f"{self.related_customer.first_name} {self.related_customer.last_name}"

    def __str__(self):
        return f"{self.related_customer}: ({self.animalname}, ₹ {self.milkprice})"


class Customerledger(models.Model):
    related_milk_category = models.ForeignKey(CustomerMilkCategory, related_name="Customerledger", on_delete=models.CASCADE, null=True)
    related_customer = models.ForeignKey(User, related_name='Customerledger', on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=1000000,db_index=True)
    price = models.FloatField(max_length=1000000,db_index=True,default=0.0)
    quantity = models.FloatField(max_length=1000000,db_index=True,default=0.0)
    total = models.FloatField(max_length=1000000,db_index=True,default=0.0)
