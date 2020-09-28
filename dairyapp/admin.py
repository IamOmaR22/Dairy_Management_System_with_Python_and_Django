from django.contrib import admin
from dairyapp.models import Vendor, MilkCategory, VendorLedger, Profile, CustomerMilkCategory
from django.contrib.auth.models import User

#********************************************#
#       ||  Vendor Classes Started  ||       #
#********************************************#
class Vendor_Admin(admin.ModelAdmin):
    list_display = ['vendorname','managername','joiningdate', 'vendorcontact']

admin.site.register(Vendor, Vendor_Admin)


class MilkCategory_Admin(admin.ModelAdmin):
    list_display = ['animalname','milkprice','related_vendor']
    list_filter = ['animalname', 'milkprice']

admin.site.register(MilkCategory, MilkCategory_Admin)


# Individual vendor dashboard
class VendorLedger_Admin(admin.ModelAdmin):
    list_display = ['related_vendor','related_milkcategory','date','price','quantity','total']
#    readonly_fields = ["price"]

admin.site.register(VendorLedger, VendorLedger_Admin)


#**********************************************#
#       ||  Customer Classes Started  ||       #
#**********************************************#

class Profile_Admin(admin.ModelAdmin):
    list_display =['__str__','user_type','contact_number','address']
admin.site.register(Profile, Profile_Admin)


class CustomerMilkCategory_Admin(admin.ModelAdmin):
    list_display = ['fullname','animalname','milkprice']
    list_filter = ['animalname', 'milkprice']
admin.site.register(CustomerMilkCategory,CustomerMilkCategory_Admin)