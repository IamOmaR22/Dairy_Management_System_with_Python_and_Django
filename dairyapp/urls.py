from django.urls import path, include
from dairyapp import views
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template

urlpatterns = [
        path('', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('accounts/',include('django.contrib.auth.urls')), # Login

        # Vendor Started
        path('addvendor/', views.addvendor, name='addvendor'),
        path('add_milk_category/',views.add_milk_category, name='add_milk_category'),
        path('allvendor/', views.allvendor, name='allvendor'),  # All vendors dashboard
        path('ledger/<int:pk>/', views.ledger, name='ledger'),  # Individual vendor dashboard

        # Customer Started
        path('addcustomer/',views.addcustomer,name='addcustomer'),
        path('customer_milk_category/',views.customer_milk_category,name='customer_milk_category'),
        path('Customer_page/',views.Customer_page,name='Customer_page'),
        path('customer_ledger/<int:pk>/', views.customer_ledger, name='customer_ledger'),  # Individual Customer dashboard
]