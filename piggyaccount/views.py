""" account app views """
from django.shortcuts import render


def piggyaccount(request):
    """ account view, returns the account.html """

    return render(request, 'piggyaccount/account.html')


def wallet(request):
    """ wallet view, returns the account.html """

    return render(request, 'piggyaccount/wallet.html')


def category(request):
    """ category view, returns the account.html """

    return render(request, 'piggyaccount/category.html')


def transaction(request):
    """ transaction view, returns the account.html """

    return render(request, 'account/transaction.html')
