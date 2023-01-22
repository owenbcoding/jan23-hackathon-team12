''' Account app admin file '''
from django.contrib import admin
from .models import Account, Wallet, Category, Transaction


class AccountAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Account model"""
    list_display = (
        'user_id',
        'name',
        'bank',
        'abalance',
        'open_date',
        'update_date',
    )


class WalletAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Wallet model"""
    list_display = (
        'account_id',
        'name',
        'category_id',
        'wbalance',
        'open_date',
        'update_date',
    )


class TransactionAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Transaction model"""
    list_display = (
        'transaction_type',
        'from_account',
        'to_account',
        'amount',
        'create_date',
        'note',
    )


class CategoryAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Category model"""
    list_display = (
        'title',
        'description',
        'user_id',
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
