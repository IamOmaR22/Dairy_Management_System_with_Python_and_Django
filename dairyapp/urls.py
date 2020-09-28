from django.urls import path, include
from dairyapp import views

urlpatterns = [
        path('', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('accounts/',include('django.contrib.auth.urls')), # Login

        # Vendor Started
        path('addvendor/', views.addvendor, name='addvendor'),
        path('add_milk_category/',views.add_milk_category, name='add_milk_category'),
        path('allvendor/', views.allvendor, name='allvendor'),  # All vendors dashboard
        path('ledger/<int:pk>/', views.ledger, name='ledger'),  # Individual vendor dashboard
]