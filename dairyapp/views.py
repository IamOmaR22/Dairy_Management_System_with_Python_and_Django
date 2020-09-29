from django.shortcuts import  redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from dairyapp import models
from django.shortcuts import get_object_or_404
from dairyapp.forms import AddVendorForm,vendorledgerForm,MilkCategoryForm,ProfileForm,SignUpForm,CustomerMilkCategoryForm,contactForm
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    title = ''
    confirm_message = None
    form = contactForm(request.POST or None)
    if form.is_valid():
        receivers_list = ['gaurav.nagar14cs003@gmail.com']
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

            return redirect('addcustomer')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def allvendor(request):
    manager=''
    if User.is_authenticated:
        manager = request.user.username
        #print(manager)
        #Vendor.objects.all().delete()
        vendor = models.Vendor.objects.filter(managername=manager)
        return render(request, 'vendor/allvendor.html',{'vendor':vendor})

@login_required
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
            return redirect('add_milk_category') # milkcategoryform.html
    else:
        form = AddVendorForm()
        return render(request, 'vendor/addvendor.html', {'form':form})

#Customer_page
def Customer_page(request):
    print("Username=",request.user)
    print("Userpk=",request.user.pk)
    customer = request.user
    customer_info = models.Customerledger.objects.filter(related_customer = customer)

    alltotal = 0.0
    for i in customer_info:
        alltotal = alltotal+float(i.total)
    print(alltotal)

    for data in customer_info:
        print("Customer Name: ",data.related_customer)
        print("joining Date: ",data.date)
        print("Quantity: ",data.price)
        print("Total: ",data.total)

    return render(request,'Customers/customer.html',{'customer_info':customer_info,'alltotal':alltotal})


#Customerleder
def customer_ledger(request,pk):
    customer_obj = get_object_or_404(User,pk=pk)
    cus_user_info = models.Profile.objects.filter(user=customer_obj)
    customer_ledger_info = models.Customerledger.objects.filter(related_customer = customer_obj)
    milktypes = models.CustomerMilkCategory.objects.filter(related_customer = customer_obj)
    milk_list = [(milk.animalname +"-"+ str(milk.milkprice), milk.pk) for milk in milktypes]

    customer_full_name = f"{customer_obj.first_name} {customer_obj.last_name}"
    alltotal = 0.0
    for i in customer_ledger_info:
        alltotal = alltotal+float(i.total)
    print(alltotal)

    return render(request,'Customers/customer_ledger.html',{
            "customer_full_name":customer_full_name,
            "milk_list":milk_list,
            "customer_obj":customer_obj,
            "customer_ledger_info":customer_ledger_info,
            "alltotal":alltotal,
            })


#Vendorledger
@login_required
def ledger(request,pk):
         ledgerform = vendorledgerForm()
         #data = vendorledger.objects.filter(managername=request.user.username)
         vendor_obj = get_object_or_404(models.Vendor,pk=pk)
        #  pkvalue = vendor_obj.pk
         #print(pkvalue)

        #  url1 = request.path
         #print(url1)

         ledgerdata = models.vendorledger.objects.filter(related_vendor=vendor_obj)
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


def customer_ledger_save(request):
    if request.method == 'POST':
        print(request.POST.dict())
        customer_pk = request.POST.get("customer", None)

        date = request.POST.get("date",None)
        milk_pk = request.POST.get("milktype", None)
        quantity = request.POST.get("quantity", None)

        related_customer  = models.User.objects.get(pk=customer_pk)
        related_milk_category = models.CustomerMilkCategory.objects.get(pk=milk_pk)
        price = related_milk_category.milkprice
        total = float(quantity) * float(price)

        data = models.Customerledger(
                related_customer = related_customer,
                date = date,
                related_milk_category = related_milk_category,
                quantity = quantity,
                price = price,
                total = total,
                )
        data.save()

        current_url = "/customer_ledger/" + str(customer_pk) + "/"

        return redirect(current_url)

def ledger_save(request):
    if request.method == 'POST':
        print(request.POST.dict())
        print(request.POST.get("milktype", ""))

        vendor_pk = request.POST.get("vendor", None)
        date = request.POST.get("date",None)
        milkcategory_pk = request.POST.get("milktype", None)
        quantity = request.POST.get("quantity", None)

        related_vendor = models.Vendor.objects.get(pk=vendor_pk)
        related_milkcategory = models.MilkCategory.objects.get(pk=milkcategory_pk)
        price = related_milkcategory.milkprice
        total = float(quantity) * float(price)
        path = request.path
        pathstr = str(path)

        #alltotal = models.vendorledger.objects.filter(pk=pk)
        #print(related_vendor,date, related_milkcategory, price, quantity, total)

        g = models.vendorledger(
            related_vendor=related_vendor,
            date = date,
            related_milkcategory=related_milkcategory,
            price=price,
            quantity=quantity,
            total=total
            )

        g.save()
        current_url = "/ledger/" + str(vendor_pk) + "/"
        return redirect(current_url)

@login_required
def add_milk_category(request):
    if request.method == 'POST':
        form = MilkCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_milk_category')
    else:
        form = MilkCategoryForm()
        return render(request,'vendor/milkcategoryform.html',{'form':form})

def ledger_delete(request):
    if request.method == 'POST':
        #print(request.POST.get('ledger_pk'))
        pk = request.POST.get('ledger_pk')
        ledger_entry = models.vendorledger.objects.get(pk=pk)
        vendor_pk = ledger_entry.related_vendor.pk
        ledger_entry.delete()
        current_url = "/ledger/" + str(vendor_pk) + "/"
    return redirect(current_url)


def customer_ledger_delete(request):
    if request.method == 'POST':
        pk = request.POST.get('customer_pk')
        customer_ledger_entry = models.Customerledger.objects.get(pk=pk)
        customer_ledger_entry.delete()
        customer_pk = customer_ledger_entry.related_customer.pk
        current_url = "/customer_ledger/" + str(customer_pk) + "/"
        return redirect(current_url)

@login_required
def addcustomer(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        print("i am in addcustomer upper")
        if form.is_valid():
            print("i am in addcustomer")
            form.save()
            return redirect('customer_milk_category')
    else:
        form = ProfileForm()
    return render(request,'Customers/Add_Customer.html',{'form':form})

@login_required
def allcustomer(request):
    customerinfo = models.Profile.objects.all()
    return render(request,'Customers/Customer_detail.html',{'customerinfo':customerinfo})

# def password_reset(request):
#     if request.method == 'POST':
#         form = password_reset_form(request.POST)
#         if form.is_valid():
#             subject = "Password Reset"
#             to_email = form.cleaned_data['email']
#             receivers_list = [to_email,]
#             message =
#
#             emailsender = settings.EMAIL_HOST_USER
#             send_mail(subject, message, emailsender, receivers_list, fail_silently=False)
#             print("To Email: ",to_email)
#             return redirect('home')
#     else:
#         form = password_reset_form()
#         return render(request,'registration/password_reset_form.html',{'form':form})

def customer_milk_category(request):
    if request.method == 'POST':
        form = CustomerMilkCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerMilkCategoryForm()
    return render(request,'Customers/customer_milk_category.html',{'form':form})
