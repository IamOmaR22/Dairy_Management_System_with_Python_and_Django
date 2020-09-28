from django.urls import path, include
from dairyapp import views

urlpatterns = [
        path('', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('accounts/',include('django.contrib.auth.urls')), # Login

        path('addvendor/', views.addvendor, name='addvendor'),
]