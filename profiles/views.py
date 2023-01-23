""" Imports for models, forms, modules """
from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Profile
from .forms import UserProfileForm


# user profile form
@login_required
def profile(request):
    """ Rendering of Profile """
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile.html")
        else:
            print(form.errors)
    else:
        form = UserProfileForm()
    return render(request, 'profile.html', {'form': form})

