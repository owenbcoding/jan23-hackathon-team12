''' Account app URL Configuration '''
from django.urls import path
from . import views

urlpatterns = [
     path('', views.piggyaccount, name='piggyaccount'),
     path('wallet', views.wallet, name='wallet'),
     path('category', views.category, name='category'),
     path('transaction', views.transaction, name='transaction'),
]