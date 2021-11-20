from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password1 = models.TextField(max_length=25)
    password2 = models.TextField(default='',max_length=25)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()