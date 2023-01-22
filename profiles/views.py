""" Imports for models, forms, modules """
from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Profile
from .forms import ProfileForm


def profile_(request):

    return render(request, 'profile.html')

