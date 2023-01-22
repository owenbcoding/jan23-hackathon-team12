""" Imports of modules, User """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ A user profile model for mantaining users """
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,
                         null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}\'s Profile'



# @receiver(post_save, sender=User)
# def create_or_update_profile(sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         Profile.objects.create(user=instance)
#     # Existing users: just save the profile
#     instance.profile.save()