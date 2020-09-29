"""MyDairy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include,path
from dairyapp import views

urlpatterns = [
        path('', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('addcustomer/',views.addcustomer,name='addcustomer'),
        path('allcustomer/',views.allcustomer,name='allcustomer'),
        path('Customer_page/',views.Customer_page,name='Customer_page'),
        path('customer_ledger_save/', views.customer_ledger_save, name='customer_ledger_save'),
        path('customer_ledger_delete/',views.customer_ledger_delete,name='customer_ledger_delete'),
        path('customer_milk_category/',views.customer_milk_category,name='customer_milk_category'),
        path('customer_ledger/<int:pk>/', views.customer_ledger, name='customer_ledger'),
        path('allvendor/', views.allvendor, name='allvendor'),
        path('addvendor/', views.addvendor, name='addvendor'),
        path('add_milk_category/',views.add_milk_category, name='add_milk_category'),
        path('ledger_save/',views.ledger_save,name='ledger_save'),
        path('ledger_delete/',views.ledger_delete,name='ledger_delete'),
        path('ledger/<int:pk>/', views.ledger, name='ledger'),
        
        path('accounts/',include('django.contrib.auth.urls')),
        path('admin/', admin.site.urls),
]
if settings.DEBUG == True or settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
