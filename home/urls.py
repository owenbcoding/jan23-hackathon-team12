from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="index"),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]