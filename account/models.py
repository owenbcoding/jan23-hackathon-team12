''' Models for account app '''
from django.db import models


class Account(models.Model):
    """Account model"""

    class Meta:
        """
        Adjust the verbose name or the plural form of it from
        the Django defaults
        """
        verbose_name_plural = 'Accounts'
    
    # user_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    bank = models.CharField(max_length=250)
    amount = models.FloatField()
    open_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return str(self.name)


class Wallet(models.Model):
    """Wallet model"""

    class Meta:
        """
        Adjust the verbose name or the plural form of it from
        the Django defaults
        """
        verbose_name_plural = 'Wallets'
    
    account_id = models.ForeignKey('Account',null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    category_id = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    open_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)


class Transaction(models.Model):
    """Transaction model"""

    class Meta:
        """
        Adjust the verbose name or the plural form of it from
        the Django defaults
        """
        verbose_name_plural = 'Transactions'
    
    transaction_type = models.CharField(max_length=250, null=True, blank=True,)
    from_account = models.CharField(max_length=250, null=True, blank=True,)
    to_account = models.CharField(max_length=250, null=True, blank=True,)
    amount = models.FloatField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    note = models.TextField(max_length=250, null=True, blank=True,)
    
    def __str__(self):
        return str(self.name)


class Category(models.Model):
    """Category model"""

    class Meta:
        """
        Adjust the verbose name or the plural form of it from
        the Django defaults
        """
        verbose_name_plural = 'Categories'
    
    title = models.CharField(max_length=250, null=True, blank=True,)
    description = models.TextField(max_length=250, null=True, blank=True,)
    # user_id = models.ForeignKey('Profile',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
