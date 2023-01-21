from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')


def team(request):
    """ A view to return the about page """
    return render(request, 'home/team.html')


def contact(request):
    """ A view to return the about page """
    return render(request, 'home/contact.html')