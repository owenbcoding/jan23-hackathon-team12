""" account app views """
from django.shortcuts import render


def account(request):
    """ account view, returns the account.html """

    return render(request, 'account/account.html')


def wallet(request):
    """ wallet view, returns the account.html """

    return render(request, 'account/wallet.html')
