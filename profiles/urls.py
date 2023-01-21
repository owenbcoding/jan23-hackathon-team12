""" Imports for modules and views """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_, name="profile"),

]