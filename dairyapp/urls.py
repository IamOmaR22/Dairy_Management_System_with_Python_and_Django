from django.urls import path, include
from dairyapp import views
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
        path('ledger_save/',views.ledger_save,name='ledger_save'),
        path('ledger_delete/',views.ledger_delete,name='ledger_delete'),

        # Customer Started
        path('addcustomer/',views.addcustomer,name='addcustomer'),  # Add Customer - This is a Profile model (For Create Admin/Manager/Customer)
        path('customer_milk_category/',views.customer_milk_category,name='customer_milk_category'),
        path('allcustomer/',views.allcustomer,name='allcustomer'),
        path('customer_ledger/<int:pk>/', views.customer_ledger, name='customer_ledger'),  # Individual Customer dashboard
        path('customer_ledger_save/', views.customer_ledger_save, name='customer_ledger_save'),
        path('customer_ledger_delete/',views.customer_ledger_delete,name='customer_ledger_delete'),
        path('Customer_page/',views.Customer_page,name='Customer_page'),
]






# from django.urls import path, include
# from django.template.loader import get_template
# from dairyapp import views

# urlpatterns = [
#         path('', views.home, name='home'),
#         path('signup/', views.signup, name='signup'),
#         path('addcustomer/',views.addcustomer,name='addcustomer'),
#         path('allcustomer/',views.allcustomer,name='allcustomer'),
#         path('Customer_page/',views.Customer_page,name='Customer_page'),
#         path('customer_ledger_save/', views.customer_ledger_save, name='customer_ledger_save'),
#         path('customer_ledger_delete/',views.customer_ledger_delete,name='customer_ledger_delete'),
#         path('customer_milk_category/',views.customer_milk_category,name='customer_milk_category'),
#         path('customer_ledger/<int:pk>/', views.customer_ledger, name='customer_ledger'),
#         path('allvendor/', views.allvendor, name='allvendor'),
#         path('addvendor/', views.addvendor, name='addvendor'),
#         path('add_milk_category/',views.add_milk_category, name='add_milk_category'),
#         path('ledger_save/',views.ledger_save,name='ledger_save'),
#         path('ledger_delete/',views.ledger_delete,name='ledger_delete'),
#         path('ledger/<int:pk>/', views.ledger, name='ledger'),
        
#         path('accounts/',include('django.contrib.auth.urls')),
# ]