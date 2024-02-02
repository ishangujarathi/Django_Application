from django.db.models.signals import post_save  #This is signal that gets fired when an object is saved.
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#We want to implement a functionality to create a user profile for each new user, instead of everytime going to django admin panel and creating a new one!

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()