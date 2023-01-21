""" account app views """
from django.shortcuts import render

def account(request):
    """ account view, returns the account.html """

    return render(request, 'account/account.html')
