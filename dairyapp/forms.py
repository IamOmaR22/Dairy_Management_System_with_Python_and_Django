from django import forms
from django.shortcuts import get_object_or_404
from dairyapp.models import MilkCategory, Vendor, Profile, CustomerMilkCategory,Customerledger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)# help_text='Optional.'
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','user_type','contact_number','joining_data','address')

class MilkCategoryForm(forms.ModelForm):
    class Meta:
        model = MilkCategory
        fields = ('animalname', 'milkprice','related_vendor')

class CustomerMilkCategoryForm(forms.ModelForm):
    class Meta:
        model = CustomerMilkCategory
        fields = ('animalname','milkprice','related_customer')

class AddVendorForm(forms.Form):
    CHOICES = (
        ('Cow','Cow'),
        ('Buffaloe','Buffaloe'),
        ('Others','Others'),
    )
    Manager_Name = forms.CharField(required=True, max_length=200)
    Vendor_Name = forms.CharField(required=True, max_length=200)
    joining_date = forms.DateField(initial=datetime.date.today)
    Address = forms.CharField(required=True)
    Vendor_Contact = forms.CharField(required=True)
    Status =  forms.BooleanField(required=False,initial=True)


class vendorledgerForm(forms.Form):
    # def __init__(self,*arg,**kwarg):
    #     print(arg)
    #     print(**kwarg)
    CHOICES1 = (
        ('Cow','Cow'),
        ('Buffaloe','Buffaloe'),
        ('Others','Others'),
    )
    CHOICES2 = (
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    )
    Milk_Category = forms.ChoiceField(label='',choices=CHOICES1)
    #Vendor_Name = forms.CharField(label='',required=True, max_length=200)
    #Manager_Name = forms.CharField(label='',required=True, max_length=200)
    Day = forms.ChoiceField(label='',choices=CHOICES2)
    Quantity = forms.CharField(label='',required=False)

class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    subject = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control','cols':20, 'rows':3 }))
