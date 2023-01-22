''' Account app admin file '''
from django.contrib import admin
from .models import Account, Wallet, Category, Transaction



admin.site.register(Account)
admin.site.register(Wallet)
admin.site.register(Category)
admin.site.register(Transaction)
