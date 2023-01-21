""" Imports for models, forms, modules """
from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Profile
from .forms import ProfileForm


def profile(request):
    """ Display the user's profile. """
    profile_all = Profile.objects.all()
    form = ProfileForm()
    context = {
        'profile_all': profile_all,
        'form': form
    }
    return render(request, 'profile.html', context)


