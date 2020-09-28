from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from dairyapp.forms import contactForm, SignUpForm, AddVendorForm, MilkCategoryForm, VendorledgerForm
from django.core.mail import send_mail
from django.conf import settings
from dairyapp import models

# Create your views here.

def home(request):
    title = ''
    confirm_message = None
    form = contactForm(request.POST or None)
    if form.is_valid():
        receivers_list = ['omarfaruk2468@gmail.com']
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['message']
        emailFrom = form.cleaned_data['email']
        message = f'Name: {name}\nEmail Id: {emailFrom}\nMessage: {comment}'
        emailsender = settings.EMAIL_HOST_USER
        send_mail(subject, message, emailsender, receivers_list, fail_silently=False)
        title ="Thanks!"+' '+name
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None
    context = {'title': title, 'form':form, 'confirm_message': confirm_message}
    temp = 'home.html'
    return render(request, temp, context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # If you want to login user after signup, than use this code
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)

            # return redirect('addcustomer')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

#*******************************************#
#       ||  Vendors Views Started  ||       #
#*******************************************#

# @login_required
def addvendor(request):
    if request.method == 'POST':
        form = AddVendorForm(request.POST)
        if form.is_valid():
            managername = form.cleaned_data['Manager_Name']
            vendorname = form.cleaned_data['Vendor_Name']
            address = form.cleaned_data['Address']
            vendorcontact = form.cleaned_data['Vendor_Contact']

            status  = form.cleaned_data['Status']

            v = models.Vendor(managername=managername,vendorname=vendorname,address=address,vendorcontact=vendorcontact,status=status)
            v.save()
            # return redirect('add_milk_category') # milkcategoryform.html
            return redirect('home')
    else:
        form = AddVendorForm()
        return render(request, 'vendor/addvendor.html', {'form':form})

# @login_required
def add_milk_category(request):
    if request.method == 'POST':
        form = MilkCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_milk_category')
    else:
        form = MilkCategoryForm()
        return render(request,'vendor/milkcategoryform.html', {'form':form})

# All vendors dashboard
# @login_required
def allvendor(request):
    manager=''
    if User.is_authenticated:
        manager = request.user.username
        #print(manager)
        #Vendor.objects.all().delete()
        vendor = models.Vendor.objects.filter(managername=manager)
        return render(request, 'vendor/allvendor.html', {'vendor':vendor})


# Individual vendor dashboard
# @login_required
def ledger(request,pk):
         ledgerform = VendorledgerForm()
         #data = VendorLedger.objects.filter(managername=request.user.username)
         vendor_obj = get_object_or_404(models.Vendor,pk=pk)
        #  pkvalue = vendor_obj.pk
         #print(pkvalue)

        #  url1 = request.path
         #print(url1)

         ledgerdata = models.VendorLedger.objects.filter(related_vendor=vendor_obj)
         alltotal=0.0
         #print(ledgerdata[0].total)
         for alto in ledgerdata:
             alltotal = alltotal+float(alto.total)

         print(alltotal)
         #print(vendor_obj)

         #print(ledgerdata)
         milks = models.MilkCategory.objects.filter(related_vendor=vendor_obj)

         #for milk in milks:
         #    print(milk.animalname + "-----" +milk.milkprice)

         milk_list = [(milk.animalname +"-"+ str(milk.milkprice), milk.pk) for milk in milks]
         print(milk_list)

         # print(tuple(milk_list))


         day_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
         return render(request, 'vendor/vendorledger.html',{
             "vendor_obj":vendor_obj,
             "ledgerdata":ledgerdata,
             "ledgerform":ledgerform,
             "num_range":range(6),
             "milk_list":milk_list,
             "day_list":day_list,
             "alltotal":alltotal,
             })