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
    
    def __str__(self):
        return str(self.name)
