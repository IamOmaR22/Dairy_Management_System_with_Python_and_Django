from django.contrib import admin
from dairyapp.models import Vendor
from django.contrib.auth.models import User

#********************************************#
#       ||  Vendor Classes Started  ||       #
#********************************************#
class Vendor_Admin(admin.ModelAdmin):
    list_display = ['vendorname','managername','joiningdate', 'vendorcontact']

admin.site.register(Vendor, Vendor_Admin)
