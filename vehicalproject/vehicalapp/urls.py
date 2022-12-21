
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('custsignup',views.customersignup,name="custsignup"),
    path('customersignin',views.customersignin,name="customersignin"),
]
