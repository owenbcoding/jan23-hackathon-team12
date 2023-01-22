""" account app views """
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from piggyaccount.models import Account
from .forms import AccountForm

@login_required
def piggyaccount(request):
    """ Rendering of Account """
    paccount = Account.objects.all()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            # we need a user feedback message here
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = AccountForm()
    return render(request, 'piggyaccount/account.html', {'form': form})


def wallet(request):
    """ wallet view, returns the account.html """

    return render(request, 'piggyaccount/wallet.html')


def category(request):
    """ category view, returns the account.html """

    return render(request, 'piggyaccount/category.html')


def transaction(request):
    """ transaction view, returns the account.html """

    return render(request, 'piggyaccount/transaction.html')
