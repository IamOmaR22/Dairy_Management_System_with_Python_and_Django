from django.contrib import admin
from dairyapp.models import Profile, Vendor, MilkCategory, vendorledger, CustomerMilkCategory,Customerledger
from django.contrib.auth.models import User


class Vendor_Admin(admin.ModelAdmin):
    list_display = ['vendorname','managername','joiningdate', 'vendorcontact']

admin.site.register(Vendor, Vendor_Admin)

class MilkCategory_Admin(admin.ModelAdmin):
    list_display = ['animalname','milkprice','related_vendor']
    list_filter = ['animalname', 'milkprice']

admin.site.register(MilkCategory, MilkCategory_Admin)

class vendorledger_Admin(admin.ModelAdmin):
    list_display = ['related_vendor','related_milkcategory','date','price','quantity','total']
#    readonly_fields = ["price"]

admin.site.register(vendorledger,vendorledger_Admin)

#****************************************************************************************************
# Customer classes
#****************************************************************************************************

class Profile_Admin(admin.ModelAdmin):
    list_display =['__str__','user_type','contact_number','address']
admin.site.register(Profile,Profile_Admin)

class CustomerMilkCategory_Admin(admin.ModelAdmin):
    list_display = ['fullname','animalname','milkprice']
    list_filter = ['animalname', 'milkprice']
admin.site.register(CustomerMilkCategory,CustomerMilkCategory_Admin)

class Customerledger_Admin(admin.ModelAdmin):
    list_display = ['related_customer','date','quantity','price','total']
admin.site.register(Customerledger,Customerledger_Admin)
