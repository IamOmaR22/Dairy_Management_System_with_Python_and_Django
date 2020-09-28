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
